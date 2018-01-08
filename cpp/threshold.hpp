#ifndef THRESHOLD_HPP
#define THRESHOLD_HPP
#include <vector>

using std::vector;

using Tensor3D = vector<vector<vector<double> > >;
using Tensor3B = vector<vector<vector<bool> > >;

bool initTensor(Tensor3B& mask, const Tensor3D& tensor);

Tensor3B threshold(const Tensor3D& tensor, double cutoff);

#endif  // THRESHOLD_HPP
