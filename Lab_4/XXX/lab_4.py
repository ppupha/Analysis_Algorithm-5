
import time
import matplotlib.pyplot as plt
import random, string
from threading import Thread
import threading
import os
import multiprocessing

class Matrix:
    def __init__(self, mat = None, row=0, col=0):
        self.mat = mat
        self.row = row
        self.col = col

class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        #print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

Val1 = -10
Val2 = 10

def matrix_random_create(row, col):
    a = [[random.randint(Val1, Val2) for j in range(col)]for i in range(row)]
    return Matrix(a, row ,col)

def matrix_create(row, col):
    a = [[0 for j in range(col)]for i in range(row)]
    return Matrix(a, row ,col)

def matrix_print(Mat):
    mat = Mat.mat
    row = Mat.row
    col = Mat.col
    for i in range(row):
        for j in range(col):
            print(mat[i][j], "  ", end = " ")
        print()
    print()

# k * 2 = k << 1
# III + IV
# = -> +=
def matrix_mult_5(A, B):

    if A.col != B.row:
        return Mat()
    M = A.row
    N = A.col
    Q = B.col
    Ndiv2 = N // 2
    Nmin1 = N - 1
    
    # I
    mulV = [0 for i in range(Q)]
    for j in range(Q):
        for k in range(0, Nmin1, 2):
            mulV[j] += B.mat[k][j] * B.mat[k + 1][j]

    #II
    mulH = [0 for i in range(M)]
    for i in range(M):
        for k in range(0, Nmin1, 2):
            mulH[i] += A.mat[i][k] * A.mat[i][k + 1]

    #III
    C = matrix_create(M, Q)

    if (N % 2 == 1):
        for i in range(M):
            for j in range(Q):
                C.mat[i][j] = -mulH[i] - mulV[j] + A.mat[i][Nmin1] * B.mat[Nmin1][j]
                for k in range(0, Nmin1, 2):
                    C.mat[i][j] += (A.mat[i][k] + B.mat[k + 1][j]) * (A.mat[i][k + 1] + B.mat[k][j])

            #IV
            
    else:
        for i in range(M):
            for j in range(Q):
                C.mat[i][j] = -mulH[i] - mulV[j]
                for k in range(0, Nmin1, 2):
                    C.mat[i][j] += (A.mat[i][k] + B.mat[k + 1][j]) * (A.mat[i][k + 1] + B.mat[k][j])
        

    return C

def timer(fn, rep = 3):
    def wrapper(*args, **kwargs):
        print(fn.__name__)
        start_time = time.time()
        for i in range(rep):
            result = fn(*args, **kwargs)
        end_time = time.time()
        print("Time = ", (end_time - start_time) * 1000 / rep)
        return (end_time - start_time) * 1000 / rep
    return wrapper


def matrix_cmp(A, B):
    if (A.row != B.row or A.col != B.col):
        return False
    M = A.row
    N = A.col
    for i in range(M):
        for j in range(N):
            if (A.mat[i][j] != B.mat[i][j]):
                return False
    return True

def tester(M, N, Q):
    A = matrix_random_create(M, N)
    B = matrix_random_create(N, Q)
    mat_Ar = [fn(A, B) for fn in fn_Ar]
    ar_len = len(fn_Ar)
    for i in range(1, ar_len):
        if (not matrix_cmp(mat_Ar[0], mat_Ar[i])):
            return False
    return True

def func_test():
    ntest = 50
    A = 0
    B = 30
    for i in range(ntest):
        M, N, Q = random.randint(A, B), random.randint(A, B), random.randint(A, B)
        res = tester(M, N, Q)
        if (not res):
            print("\t\t\tTest {}: {}".format(i, res))
        else:
            print("Test {}: {}".format(i, res))
    print("Test Finish")   

def graph_draw(matrix_size = [100, 200, 300, 400, 500, 600, 700, 800,]):
    print("Check in")
    print("Matrix Creating...")
    MatrixA = [matrix_random_create(size, size) for size in matrix_size]
    MatrixB = [matrix_random_create(size, size) for size in matrix_size]
    #rep = 1
    len_size = len(matrix_size)
    len_Ar = len(fn_Ar)
    print("Timing...")    
    time_Ar = [[fn_timer(MatrixA[i], MatrixB[i], num_Thr) for i in range(len_size)] for num_Thr in num_thrArr]
    print(time_Ar)
    label_Ar = ["1", "2", "4", "8", "16", "32" ]
    format_Ar = ["bo-", "ro-", "go-", "yo-", "ko-", "co-"]
    print("Drawing...")
    
    for i in range(len(time_Ar)):
        plt.plot(matrix_size, time_Ar[i], format_Ar[i], label = label_Ar[i])
    plt.xlabel("len")
    plt.ylabel("time(ms)")
    plt.legend(loc = "best")
    plt.show()

def parallel(func, args, M, num_thread):
    count = M // num_thread
    threads = []
    tmp = list(args)
    start, end = 0, 0
    for i in range(num_thread):
        if i == num_thread - 1:
            end = M
        else:
            end = start + count
        tmp.append(start)
        tmp.append(end)
        
        f_args = tuple(tmp)   
        t = Thread(target = func, args = f_args)
        threads.append(t)
        t.start()
        
        tmp.pop()
        tmp.pop()
        start += count

    for t in threads:
        t.join()


def calc_MulV(B, mulV, start = 0, end = None):
    if end == None:
        end = start + 1
    Nmin1 = B.row - 1
    for j in range(start, end):
        for k in range(0, Nmin1, 2):
            mulV[j] += B.mat[k][j] * B.mat[k + 1][j]

def calc_MulH(A, mulH, start = 0, end = None):
    if end == None:
        end = start + 1
    Nmin1 = A.col - 1
    for i in range(start, end):
        for k in range(0, Nmin1, 2):
            mulH[i] += A.mat[i][k] * A.mat[i][k + 1]

def part3_parallel(A, B, C, mulH, mulV, start, end):
    Nmin1 = A.col - 1 
    Q = B.col
    for i in range(start, end):
        for j in range(Q):
            C.mat[i][j] = -mulH[i] - mulV[j]
            for k in range(0, Nmin1, 2):
                C.mat[i][j] += (A.mat[i][k] + B.mat[k + 1][j]) * (A.mat[i][k + 1] + B.mat[k][j])

def part4_parallel(A, B, C, mulH, mulV, start, end):
    Nmin1 = A.col - 1
    Q = B.col
    Nmin1 = A.col - 1
    for i in range(start, end):
            for j in range(Q):
                C.mat[i][j] = C.mat[i][j] + A.mat[i][Nmin1] * B.mat[Nmin1][j]

def mult_parallel(A, B, num_threads = None):

    if A.col != B.row:
        return Mat()
    M = A.row
    N = A.col
    Q = B.col
    Nmin1 = N - 1
    #Get Thread_Count
    if num_threads == None:
        try:
            num_threads = multiprocessing.cpu_count()
        except AttributeError:
            num_threads = 4
            
    mulV = [0 for i in range(Q)]
    mulH = [0 for i in range(M)]
    
    if (num_threads >= 2):
        #I
        t1 = Thread(target = parallel, args = (calc_MulV, (B, mulV), Q, num_threads // 2))
        t1.start()
        #II
        t2 = Thread(target = parallel, args = (calc_MulH, (A, mulH, ), M, num_threads - num_threads // 2))
        t2.start()
        t1.join()
        t2.join()
    else:
        # I
        for j in range(Q):
            for k in range(0, Nmin1, 2):
                mulV[j] += B.mat[k][j] * B.mat[k + 1][j]

        #II
        for i in range(M):
            for k in range(0, Nmin1, 2):
                mulH[i] += A.mat[i][k] * A.mat[i][k + 1]
                
    #III
    C = matrix_create(M, Q)
    parallel(part3_parallel, (A, B, C, mulH, mulV), M, num_threads)

    #IV      
    if (N % 2 == 1):
        parallel(part4_parallel, (A, B, C, mulH, mulV), M, num_threads)
    return C
    
fn_Ar = [mult_parallel,matrix_mult_5]
fn_Name = ["алгоритм Винограда Paralle", "Алгоритм Винограда"]
rep = 1
fn_timer = timer(fn_Ar[0], rep)
num_thrArr = [1, 2, 4, 8,]# 16, 32]
def test():
    print("Check in")
    matrix_size = [101, 201, 301, 400,]
    print("Matrix Creating...")
    MatrixA = [matrix_random_create(size, size) for size in matrix_size]
    MatrixB = [matrix_random_create(size, size) for size in matrix_size]
    
    len_size = len(matrix_size)
    len_Ar = len(fn_Ar)
    print("Timing...")
    for i in range(len_size):
        for fn in fn_timer_Ar:
            fn(MatrixA[i], MatrixB[i])

#test()

def matrix_input():
    m = int(input('number of rows, m = '))
    n = int(input('number of columns, n = '))

    mat = [list(map(int, input().split())) for i in range(0, m)]
    return Matrix(mat, m, n)

def matrix_mult():
    try:
        A = matrix_input()
        B = matrix_input()
        print("Matrix A")
        matrix_print(A)
        print("Matrix B")
        matrix_print(B)
        num_thread = int(input("Input Num_Thread: "))
        print("Matrix C = AxB")
        C = mult_parallel(A, B, num_thread)
        print("\n\nNum_thread = {}".format(num_thread))
        matrix_print(C)
    except:
        print("Error")

def grap():
    try:
        
        size1 = [10, 20, 30, 40, 50, 60, 70, 80]
        size2 = [i for i in range(100, 801, 100)]
        size3 = [i for i in range(100, 301, 30)]
        size_arr = [size1, size2, size3]
        print("1. size 1: ", size1)
        print("2. size 2: ", size2)
        print("3. size 3: ", size3)
        s = int(input("input size (Рекомендовано Size 1): "))
        if (s == 1):
            global fn_timer_Ar
            fn_timer_Ar = [timer(fn, 2000) for fn in fn_Ar]
        print("Choose: ", size_arr[s - 1])
        graph_draw(size_arr[s - 1])
    except:
        print("Errorr")

def menu():
    print("0. Exit")
    print("1. Matrix Mult")
    print("2. Test Func")
    print("3. Time")
    count = 3
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
            matrix_mult()
        elif (c == 2):
            func_test()
        elif (c == 3):
            grap()
        

main()



M = 5
N = 5
Q = 5
A = matrix_random_create(M, N)
print("Matrix A: ")
matrix_print(A)
B = matrix_random_create(N, Q)
print("Matrix B: ")
matrix_print(B)

num = [1, 2, 4, 8]
for i in num:
    print("\n\nNum_thread = {}".format(i))
    C = mult_parallel(A, B, i)
    matrix_print(C)












'''
def mulV_parall(B, num_thread = 1):
    Q = B.col
    mulV = [0 for i in range(Q)]
    
    parallel(calc_MulV, (B, mulV, ), Q, num_thread)
        
    return mulV

def mulH_parall(A, num_thread = 1):
    Nmin1 = A.col - 1
    M = A.row
    mulH = [0 for i in range(M)]

    parallel(calc_MulH, (A, mulH, ), M, num_thread) 
            
    return mulH

'''

