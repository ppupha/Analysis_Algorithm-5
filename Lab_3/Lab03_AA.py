import random
import matplotlib.pyplot as plt
import time

Max_Value = 100000
Max_Len_Arr = 1000

def swap(a, b):
    a, b = b, a
    return a, b

def random_arr(n):
    return [random.randint(0, Max_Value) for i in range(n)]

def arr_cmp(a, b):
    na = len(a)
    nb = len(b)
    if (na != nb):
        return False
    for i in range(na):
        if a[i] != b[i]:
            return False

    return True

def check_mat(mat):
    n = len(mat)
    for i in range(1, n):
        fl = arr_cmp(mat[i-1], mat[i])
        if (not fl):
            return False
    return True

def bubbleSort(a):
    n = len(a)
    nmin1 = n - 1
    for i in range(nmin1):
        for j in range(nmin1, i, -1):
            if (a[j-1] > a[j]):
                tmp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tmp
    return a


def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        tmp = a[i]
        j = i - 1
        while ( j >= 0) and (tmp < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = tmp
    return a

def shellSort(a):
    n = len(a)
    h = n // 2
    while (h > 0):
        for i in range(h, n):
            tmp = a[i]
            j = i - h
            while (j >= 0 and a[j] > tmp):
                a[j+h] = a[j]
                j = j - h
            a[j+h] = tmp
        h = h // 2
    return a

def distributionCounting(a):
    M = Max_Value
    Mplus1 = M + 1
    n = len(a)
    c = [0 for i in range(Mplus1)]
    x = a.copy()

    for i in range(n):
        c[a[i]] += 1

    c[0] -= 1

    for v in range(1, Mplus1):
        c[v] += c[v-1]

    for i in range(n-1, -1, -1):
        v = x[i]
        a[c[v]] = x[i]
        c[v] -= 1
    return a

def timer(fn, rep = 5):
    def wrapper(*args, **kwargs):
        print(fn.__name__)
        start_time = time.time()
        for i in range(rep):
            result = fn(*args, **kwargs)
        end_time = time.time()
        #print('total run-time of {}: {} ms'.format(fn.__name__, (end_time - start_time) * 1000 / rep))
        print("Time = ", (end_time - start_time) * 1000 / rep)
        return (end_time - start_time) * 1000 / rep
    return wrapper

def draw_graph(fl = 2):
        global Max_Value
        Max_Value = int(input("Input Max Value in Array: "))
        arr_size = [100, 200, 500, 1000, 2000, 5000, 10000, 20000,]
        #arr_size = [i for i in range(100, 1001, 100)]#[100, 200, 500, 800, 1000, 2000, 5000]
        len_size = len(arr_size)
        print("Data Creating...")
        src = [random_arr(size) for size in arr_size]
        
        if fl == 0: # Sorted Inc Array
            for a in src:
                a.sort()
        elif fl == 1: #Sorted Dec Array
            for a in src:
                a.sort(reverse = True)
        #else Random Array
                
        arr = [[src[i].copy() for i in range(len_size)] for j in range(fn_len)]

        print("Timing...")
        time_Ar = [[fn_timer[i](a) for a in arr[i]] for i in range(fn_len)]

        print("Drawing...")
        label_arr = ["Bubble Sort", "Insertion Sort", "Distribution Counting"]
        format_arr = ["bo-", "ro-", "go-", "yo-", "ko-"]

        for i in range(fn_len):
            plt.plot(arr_size, time_Ar[i], format_arr[i], label = label_arr[i])
        plt.xlabel("Len")
        plt.ylabel("Time(ms)")
        plt.legend(loc = "best")
        plt.show()
        
fn_arr = [bubbleSort, insertionSort, distributionCounting,]
fn_name = ["Bubble Sort", "Insertion Sort", "Distric Counting"]
fn_len = len(fn_arr)
fn_timer = [timer(fn) for fn in fn_arr]


def test(n = 10):
    a = random_arr(n)
    arr = [a.copy() for i in range(fn_len)]
    for i in range(fn_len):
        fn_arr[i](arr[i])
    fl = check_mat(arr)
    if (not fl):
        print(a)
        print(arr[2])
    return fl

def tester(test_len = 20):
    len_arr = [random.randint(1, Max_Len_Arr) for i in range(test_len)]
    for i in range(test_len):
        fl = test(len_arr[i])
        if not fl:
            print("\t\t\t {}: {}".format(i, fl))
        else:
            print("Test {}: {}".format(i, fl))
    print("Finish")

def sort_arr():
    a = list(map(int, input("Input Array").split(" ")))
    n = len(a)
    print("Input: ")
    print(a)
    print("Sorted" )
    for i in range(fn_len):
        b = a.copy()
        print(fn_name[i])
        print(fn_arr[i](b))


def menu():
    print("0. Exit")
    print("1. Array Sort")
    print("2. Test Func")
    print("3. Time with Random Array")
    print("4. Time with Sorted Inc Array")
    print("5. Time with Sorted Dec Array")
    count = 5
    while (1):
        n = int(input("Input Choose: "))
        if (n >= 0 and n <= count):
            return n
        else:
            print("Input Again")

def main():
    c = 1
    while (c != 0):
        c = menu()
        if (c == 0):
            return 0
        elif (c == 1):
            sort_arr()
        elif (c == 2):
            tester()
        elif (c == 3):
            draw_graph(fl = 2)
        elif (c == 4):
            draw_graph(fl = 0)
        elif (c == 5):
            draw_graph(fl = 1)
    
main()

    
