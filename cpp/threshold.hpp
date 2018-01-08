#ifndef THRESHOLD_HPP
#define THRESHOLD_HPP
#include <vector>

using std::vector;

using Tensor3D = vector<vector<vector<double> > >;
using Tensor3B = vector<vector<vector<bool> > >;

/**
 * Return 3D Boolean Tensor. Its element is `true` if `tensor[i][j][k] > cutoff`
 *
 * @param tensor 3D Tensor of shape (H, W, D)
 * @param cutoff threshold value between 0 and 1
 *
 * @return Tensor3B 3D Boolean Tensor
 */
Tensor3B threshold(const Tensor3D& tensor, double cutoff);

/**
 * Pointer version of `threshold` because vector conversion is slow in FFI
 *
 * @param tensor 3D Tensor of shape (H, W, D)
 * @param h Height
 * @param w Width
 * @param d Depth
 * @param cutoff threshold value beteen 0 and 1
 *
 * @return Tensor3B 3D Boolean Tensor
 */
Tensor3B threshold_use_ptr(double* tensor, int h, int w, int d, double cutoff);
#endif  // THRESHOLD_HPP
