import zipfile
import numpy as np
import os

from PIL import Image
from dicom_import import dicom_datasets_from_zip, combine_slices

try:
    from threshold import threshold_cpp_ptr as threshold_cpp
except:
    raise ImportError("Please run `make cython` to build dependencies")


def rescale(image, output_min=0.0, output_max=1.0):
    input_min = np.amin(image)
    input_max = np.amax(image)
    return (image - input_min) * (output_max - output_min) / (
        input_max - input_min) + output_min


def threshold(voxels, cutoff, use_cpp=False):
    '''
    Replace this function with one that calls your C or C++ implementation of `threshold`.
    '''
    if use_cpp:
        return threshold_cpp(voxels, cutoff)

    thresholded = np.zeros(voxels.shape, dtype=bool)
    thresholded[voxels > cutoff] = True
    return thresholded


def write_slices_as_pngs(path: str, voxels: np.ndarray) -> bool:
    '''
    Write the axial slices of the CT scan to individual png files.
    For file names, you can simply number the slices.
    '''
    voxels = np.uint8(voxels * 255)

    _, _, D = voxels.shape

    os.makedirs(path, exist_ok=True)

    try:
        for i in range(D):
            im = Image.fromarray(voxels[..., i])
            im.save(os.path.join(path, "{}.png".format(i)))

        return True

    except:
        return False


def main(flags):
    """Main Function"""
    if not os.path.exists(flags.FILE):
        raise FileNotFoundError(
            "{} is not found. Please run `make download` to download data".
            format(flags.FILE))

    with zipfile.ZipFile(flags.FILE, 'r') as f:
        dicom_datasets = dicom_datasets_from_zip(f)

    voxels_int16, _ = combine_slices(dicom_datasets)
    voxels_float = voxels_int16.astype(dtype=float)

    voxels_normalized = rescale(voxels_float, 0.0, 1.0)
    voxels_thresholded = threshold(voxels_normalized, cutoff=0.4, use_cpp=True)

    ret = write_slices_as_pngs(flags.DEST, voxels_thresholded)
    if not ret:
        print("[FAIL] couldn't write png files")
    else:
        print("[Success] output files are located in {} directories".format(
            flags.DEST))


if __name__ == "__main__":
    # Flags
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--file",
        default="./data/example-lung-ct.zip",
        type=str,
        dest="FILE",
        help="Path to lung ct zip file")

    parser.add_argument(
        "--dest",
        default="exported",
        type=str,
        dest="DEST",
        help="Destination directory to save PNG files")
    flags = parser.parse_args()
    main(flags)
