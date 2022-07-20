
#include <time.h>
#include <functional>

double check_time(const std::function<void()>& f) {
    int n = 1;
    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        f();
    }
    clock_t end = clock();
    return static_cast<double>(end - start) / CLOCKS_PER_SEC / n;
}