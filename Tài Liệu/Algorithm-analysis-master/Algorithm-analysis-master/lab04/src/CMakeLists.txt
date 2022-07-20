project(matrix_multiplication)
set(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++11 -pthread")

add_executable(matrix_multiplication main.cpp parallel_vinograd.cpp parallel_vinograd.h
        ../lab02/matrix_multiplication.cpp
        ../lab02/matrix_multiplication.h)
add_executable(test test.cpp parallel_vinograd.cpp parallel_vinograd.h
        ../lab02/matrix_multiplication.cpp
        ../lab02/matrix_multiplication.h)