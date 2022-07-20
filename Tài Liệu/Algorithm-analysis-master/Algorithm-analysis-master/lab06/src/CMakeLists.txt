cmake_minimum_required(VERSION 3.13)
project(lab06)

set(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")


add_executable(lab06 main.cpp Graph.cpp Graph.h Colony.cpp Colony.h exhaustive_search.cpp exhaustive_search.h)