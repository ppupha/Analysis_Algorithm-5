import time


def timer(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print('total run-time of {}: {} ms'.format(fn.__name__, (end_time - start_time) * 1000))
        return result
    return wrapper

def add(x, y):
    return x + y

add_t = timer(add)

def sub(x, y):
    return x - y

sub_t = timer(sub)

# test
add_t(3, 4)
sub_t(3, 4)
# test
add_t(3, 4)
sub(3, 4)
