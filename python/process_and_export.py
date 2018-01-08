import zipfile
import numpy as np
from dicom_import import dicom_datasets_from_zip, combine_slices


def rescale(image, output_min=0.0, output_max=1.0):
    input_min = np.amin(image)
    input_max = np.amax(image)
    return (image - input_min) * (output_max - output_min) / (
        input_max - input_min) + output_min


def threshold(voxels, cutoff):
    '''
    Replace this function with one that calls your C or C++ implementation of `threshold`.
    '''
    thresholded = np.zeros(voxels.shape, dtype=bool)
    thresholded[voxels > cutoff] = True
    return thresholded


def write_slices_as_pngs(path, voxels):
    '''
    Write the axial slices of the CT scan to individual png files.
    For file names, you can simply number the slices.
    '''
    return None


if __name__ == "__main__":
    # Flags
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("FILE", type=str)
    flags = parser.parse_args()

    with zipfile.ZipFile(flags.FILE, 'r') as f:
        dicom_datasets = dicom_datasets_from_zip(f)

    voxels_int16, _ = combine_slices(dicom_datasets)
    voxels_float = voxels_int16.astype(dtype=float)

    voxels_normalized = rescale(voxels_float, 0.0, 1.0)
    voxels_thresholded = threshold(voxels_normalized, cutoff=0.4)

    write_slices_as_pngs('exported', voxels_thresholded)
