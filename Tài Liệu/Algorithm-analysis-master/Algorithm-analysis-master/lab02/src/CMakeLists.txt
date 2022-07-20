project(matrix_multiplication)
set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_FLAGS "-O1")

add_executable(matrix_multiplication main.cpp matrix_multiplication.cpp matrix_multiplication.h)
add_executable(test test.cpp matrix_multiplication.cpp matrix_multiplication.h)