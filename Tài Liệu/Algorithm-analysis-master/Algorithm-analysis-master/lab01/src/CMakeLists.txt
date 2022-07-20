project(lev)
set(CMAKE_CXX_STANDARD 11)

add_executable(lev main.cpp levenshtein_dist.cpp levenshtein_dist.h)
add_executable(test test.cpp levenshtein_dist.cpp levenshtein_dist.h)