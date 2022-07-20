
import time
import matplotlib.pyplot as plt
import random, string

class Matrix:
    def __init__(self, mat = None, row=0, col=0):
        self.mat = mat
        self.row = row
        self.col = col

def matrix_random_create(row, col):
    a = [[random.randint(5e11, 5e12) for j in range(col)]for i in range(row)]
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

def matrix_mult_1(MatA, MatB):
    if MatA.col != MatB.row:
        return Mat()

    M = MatA.row
    N = MatA.col
    Q = MatB.col
    MatC = matrix_create(M, Q)

    for i in range(M):
        for j in range(Q):
            for k in range(N):
                MatC.mat[i][j] = MatC.mat[i][j] + MatA.mat[i][k] * MatB.mat[k][j]

    return MatC


def matrix_mult_2(A, B):
    if A.col != B.row:
        return Mat()
    
    M = A.row
    N = A.col
    Q = B.col
    # I
    mulV = [0 for i in range(Q)]
    for j in range(Q):
        for k in range(N // 2):
            mulV[j] = mulV[j] + B.mat[2 * k][j] * B.mat[2 * k + 1][j]

    #II
    mulH = [0 for i in range(M)]
    for i in range(M):
        for k in range(N // 2):
            mulH[i] = mulH[i] + A.mat[i][2 * k] * A.mat[i][2 * k + 1]

    #III
    C = matrix_create(M, Q)

    for i in range(M):
        for j in range(Q):
            C.mat[i][j] = -mulH[i] - mulV[j]
            for k in range(N // 2):
                C.mat[i][j] = C.mat[i][j] + (A.mat[i][2 * k] + B.mat[2 * k + 1][j]) * (A.mat[i][2 * k + 1] + B.mat[2 * k][j])

    #IV
    if (N % 2 == 1):
        for i in range(M):
            for j in range(Q):
                C.mat[i][j] = C.mat[i][j] + A.mat[i][N - 1] * B.mat[N - 1][j]

    return C

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
        #print('total run-time of {}: {} ms'.format(fn.__name__, (end_time - start_time) * 1000 / rep))
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
    rep = 1
    len_size = len(matrix_size)
    len_Ar = len(fn_Ar)
    print("Timing...")    
    time_Ar = [[fn(MatrixA[i], MatrixB[i]) for i in range(len_size)] for fn in fn_timer_Ar]
    print(time_Ar)
    label_Ar = ["Классический алгоритм", "Алгоритм Винограда", "Оптимизированный алгоритм Винограда" ]
    format_Ar = ["bo-", "ro-", "go-", "yo-", "ko-"]
    print("Drawing...")
    
    for i in range(len_Ar):
        plt.plot(matrix_size, time_Ar[i], format_Ar[i], label = label_Ar[i])
    plt.xlabel("len")
    plt.ylabel("time(ms)")
    plt.legend(loc = "best")
    plt.show()
    
fn_Ar = [matrix_mult_1, matrix_mult_2, matrix_mult_5,]
fn_Name = ["Классический алгоритм", "Алгоритм Винограда", "Оптимизированный алгоритм Винограда" ]
rep = 1
fn_timer_Ar = [timer(fn, rep) for fn in fn_Ar]

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
        print("Matrix C = AxB")
        for i in range(len(fn_Ar)):
            C = fn_Ar[i](A, B)
            print(fn_Name[i])
            matrix_print(C)
    except:
        print("Error")

def grap():
    try:
        
        size1 = [10, 20, 30, 40, 50, 60, 70, 80]
        size2 = [100, 200, 300, 400, 500, 600, 700, 800]
        size3 = [101, 201, 301, 401, 501, 601, 701, 801]
        size_arr = [size1, size2, size3]
        print("1. size 1: ", size1)
        print("2. size 2: ", size2)
        print("3. size 3: ", size3)
        s = int(input("input size (Рекомендовано Size 1): "))
        if (s == 1):
            global fn_timer_Ar
            fn_timer_Ar = [timer(fn, 10) for fn in fn_Ar]

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
    


