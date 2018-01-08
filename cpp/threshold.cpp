#include "threshold.hpp"

bool initTensor(Tensor3B& mask, const Tensor3D& tensor) {
  size_t height = tensor.size();
  if (!height) return false;

  size_t width = tensor[0].size();
  if (!width) return false;

  size_t depth = tensor[0][0].size();
  if (!depth) return false;

  mask.resize(height);
  for (size_t r = 0; r < height; ++r) {
    mask[r].resize(width);
    for (size_t c = 0; c < width; ++c) {
      mask[r][c].resize(depth);
    }
  }

  return true;
}

Tensor3B threshold(const Tensor3D& tensor, double cutoff) {
  Tensor3B mask;

  bool isInitialized = initTensor(mask, tensor);
  if (!isInitialized) return mask;

  for (size_t h = 0; h < tensor.size(); ++h)
    for (size_t w = 0; w < tensor[h].size(); ++w)
      for (size_t c = 0; c < tensor[h][w].size(); ++c)
        mask[h][w][c] = tensor[h][w][c] > cutoff ? true : false;

  return mask;
}
