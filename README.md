# Python / C++ Image Processing Challenge

## Get Started

### With docker

```bash
docker-compose up
```

### Without docker

1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Download dataset
    ```bash
    make download
    ```
1. Build Cython
    ```bash
    make cython
    ```
1. (optional) Run Test
    ```bash
    make test
    ```
1. Run (export CT image to exported directory)
    ```bash
    make run
    ```


## Tasks to complete

### Part I - Replace `threshold` function with a C or C++ implementation

Replace the existing `threshold` function with a C or C++ implementation that behaves the same.
You may want to add some unit tests for it.

### Part II - Write the axial slices as PNG files

Implement the body of the `write_slices_as_pngs` function to save the thresholded voxels as
multiple 2D images (slices). You can assume that the third dimension of the voxel array is the
axial dimension.
