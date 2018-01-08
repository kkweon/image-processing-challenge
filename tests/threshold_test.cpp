#include <algorithm>
#include "catch.hpp"
#include "threshold.hpp"

int sum_of(const Tensor3B& m) {
  int ret = 0;
  for (size_t row = 0; row < m.size(); ++row)
    for (size_t col = 0; col < m[row].size(); ++col)
      for (size_t depth = 0; depth < m[row][col].size(); ++depth)
        ret += m[row][col][depth];

  return ret;
}

SCENARIO(
    "threshold function works"
    "[threshold]") {
  GIVEN("Empty Tensor") {
    Tensor3D tensor = {{{}}};

    WHEN("any cutoff is given") {
      THEN("Wrong empty mask") {
        Tensor3B result = threshold(tensor, 0.7);
        REQUIRE(result.size() == 0);
      }
    }
  }

  GIVEN("Some 3D Tensor") {
    Tensor3D tensor = {{{1, 1, 1}, {0, 0, 0}}, {{0.5, 0.5, 0.5}, {0, 0, 0}}};

    WHEN("cutoff is 1") {
      THEN("Returns all false") {
        auto result = threshold(tensor, 1);
        REQUIRE(sum_of(result) == 0);
      }
    }

    WHEN("cutoff is 0.4") {
      THEN("Correct output is returned") {
        auto result = threshold(tensor, 0.4);
        REQUIRE(sum_of(result) == 6);
      }
    }
  }
}
