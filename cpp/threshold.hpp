#ifndef THRESHOLD_HPP
#define THRESHOLD_HPP
#include <vector>

using std::vector;

using Tensor3D = vector<vector<vector<double> > >;
using Tensor3B = vector<vector<vector<bool> > >;

Tensor3B threshold(const Tensor3D& tensor, double cutoff);
Tensor3B threshold_use_ptr(double* tensor, int h, int w, int d, double cutoff);
#endif  // THRESHOLD_HPP
