#include "threshold.hpp"

using std::size_t;

Tensor3B threshold(const Tensor3D& tensor, double cutoff) {
  size_t height = tensor.size();
  if (!height) return Tensor3B();

  size_t width = tensor[0].size();
  if (!width) return Tensor3B();

  size_t depth = tensor[0][0].size();
  if (!depth) return Tensor3B();

  Tensor3B mask(height,
                vector<vector<bool> >(width, vector<bool>(depth, false)));

  for (size_t h = 0; h < tensor.size(); ++h)
    for (size_t w = 0; w < tensor[h].size(); ++w)
      for (size_t c = 0; c < tensor[h][w].size(); ++c)
        mask[h][w][c] = tensor[h][w][c] > cutoff ? true : false;

  return mask;
}

Tensor3B threshold_use_ptr(
    double* tensor, int height, int width, int depth, double cutoff) {
  Tensor3B mask(height,
                vector<vector<bool> >(width, vector<bool>(depth, false)));

  for (int h = 0; h < height; ++h)
    for (int w = 0; w < width; ++w)
      for (int c = 0; c < depth; ++c) {
        int idx       = h * width * depth + w * depth + c;
        mask[h][w][c] = *(tensor+idx) > cutoff ? true : false;
      }

  return mask;
}
