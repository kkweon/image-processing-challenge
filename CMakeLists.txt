cmake_minimum_required(VERSION 3.0)
project(image_processing_challenge)

set(CMAKE_CXX_STANDARD 14)
SET (SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/threshold.cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/cpp)

set(CATCH_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/catch)
add_library(Catch INTERFACE)
target_include_directories(Catch INTERFACE ${CATCH_INCLUDE_DIR})

set(TEST_SOURCES
  ${CMAKE_CURRENT_SOURCE_DIR}/tests/test_main.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/tests/threshold_test.cpp)
add_executable(tests ${TEST_SOURCES} ${SOURCES})
target_link_libraries(tests Catch)

enable_testing()
add_test(NAME ThresholdTest COMMAND tests)
