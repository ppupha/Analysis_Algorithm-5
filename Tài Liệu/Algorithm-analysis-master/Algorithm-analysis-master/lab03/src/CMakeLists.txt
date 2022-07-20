project(sorts)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

add_executable(sorts main.cpp sorts.cpp sorts.h)
add_executable(test test.cpp sorts.cpp sorts.h)