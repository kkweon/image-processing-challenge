# Python / C++ Image Processing Challenge

## Setup

You must have Python 3 installed.

All of the python requirements are listed in `requirements.txt`.

To install:

    pip install -r requirements.txt

Verify your setup is working by running the automated tests:

    pytest

## Overview

The file `process_and_export.py` loads data from a CT scan, performs a simple threshold
operation on the voxels, and returns a binary voxel array.

## Part I - Replace `threshold` function with a C or C++ implementation

Replace the existing `threshold` function with a C or C++ implementation that behaves the same.
You may want to add some unit tests for it.

## Part II - Write the axial slices as PNG files

Implement the body of the `write_slices_as_pngs` function to save the thresholded voxels as
multiple 2D images (slices). You can assume that the third dimension of the voxel array is the
axial dimension.

## Other Details

Please do not fork this repository. Instead, work on a local copy of the repository.

As you code, create logical commits with good commit messages.

To submit your solution, please zip up your entire repository, and email it to
`info@innolitics.com`.

If you have any questions about the requirements, please ask!  Part of being a good
engineer is knowing when to clarify requirements.

## Notes

It is not good to include a large zip file (like our example ct data set) in a repository.
