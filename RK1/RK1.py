from math import *
from random import *
import time
import matplotlib.pyplot as plt

eps = 1e-5

def array_print(name, arr):
    print(name, ' ' * (10 - len(name)), end = "")
    for i in arr:
        if (i == 0):
            print('|    -', end = "")
        else:
            print('|{:>5}'.format(i), end = "")
    print()

def compareMatrix(m1, m2):
    row = len(m1)
    col = len(m1[0])
    for i in range(row):
        for j in range(col):
            if (m1[i][j] != m2[i][j]):
                return False
    return True


def createMatrix(row, col, p):
    res = [[0 for i in range(col)] for j in range(row)]
    sum = int(row * col * p)
    count = 0
    if (p < 0.9):
        for i in range(sum):
            fl = True
            while(fl):
                x = randint(0, row - 1)
                y = randint(0, col - 1)
                if (res[x][y] == 0):
                    res[x][y] = randint(1, 10)
                    fl = False
    else:
        for i in range(row):
            for j in range(col):
                tmp = randint(-5, 5)
                if tmp != 0 and count >= sum:
                    tmp = 0
                elif tmp != 0:
                    count += 1
                res[i][j] = tmp
    return res
                

def toNormalMatrix(mat):
    AN = mat[0]
    NROW = mat[1]
    NCOL = mat[2]
    JROW = mat[3]
    JCOL = mat[4]
    row = len(JROW)
    col = len(JCOL)
    #array_print('AN', AN)
    #array_print('NCOL', NCOL)
    #array_print('NROW', NROW)
    #array_print('JROW', JROW)
    #array_print('JCOL', JCOL)
    
    new = [[0 for i in range(col)] for j in range(row)]
    count = len(AN)
    for k in range(count):
        tmp = NROW[k]
        while tmp > 0 and tmp != -NROW[tmp]:
            tmp = NROW[tmp]
        if (tmp < 0):
            tmp *= -1
        i = 0
        while (i < row and tmp != JROW[i]):
            i += 1
        x = i

        tmp = NCOL[k]
        while tmp > 0 and tmp != -NCOL[tmp]:
            tmp = NCOL[tmp]
        if (tmp < 0):
            tmp *= -1
        i = 0
        while (i < col and tmp != JCOL[i]):
            i += 1
        y = i
        new[x][y] = AN[k]
        
    return new
            
def fromNomalMatrix(matrix):
    
    row = len(matrix)
    col = len(matrix[0])

    AN = []
    NROW = [-1 for i in range(row * col)]
    NCOL = [-1 for i in range(row * col)]
    JROW = [-1 for i in range(row)]
    JCOL = [-1 for i in range(col)]
    JLast = [-1 for i in range(col)]
    LastRow = [-1 for i in range(row)]
    count = -1
    for i in range(row):
        ILast = -1
        for j in range(col):
            if (matrix[i][j] != 0):
                count += 1
                AN.append(matrix[i][j])
                if (JROW[i] == -1):
                    JROW[i] = count
                if (JCOL[j] == -1):
                    JCOL[j] = count
                    
                if (ILast == -1):
                    ILast = count
                else:
                    NROW[ILast] = count
                    ILast = count
                    
                if JLast[j] ==  (-1):
                    JLast[j] = count
                else:
                    NCOL[JLast[j]] = count
                    JLast[j] = count
        if (ILast != -1):
            NROW[ILast] = -JROW[i]
            LastRow[i] = ILast

    for i in range(col):
        NCOL[JLast[i]] = -JCOL[i]
    count += 1
    AN = AN[0:count]
    NROW = NROW[0:count]
    NCOL = NCOL[0:count]

    return [AN, NROW, NCOL, JROW, JCOL, LastRow]

def plusArray(arr, value):
    for i in range(len(arr)):
        if (arr[i] <= 0):
            arr[i] = -(-arr[i] + value)
        else:
            arr[i] += value
    return arr


def connectNomalMatrix(mat1, mat2):
    row = len(mat1)
    new = []
    for i in range(row):
        row = mat1[i].copy()
        row.extend(mat2[i])
        new.append(row)
    return new

def connectMatrix(mat1, mat2):
    AN1 = mat1[0]
    NROW1 = mat1[1]
    NCOL1 = mat1[2]
    JROW1 = mat1[3]
    JCOL1 = mat1[4]
    row1 = len(JROW1)
    col1 = len(JCOL1)

    AN2 = mat2[0]
    NROW2 = mat2[1]
    NCOL2 = mat2[2]
    JROW2 = mat2[3]
    JCOL2 = mat2[4]
    
    row2 = len(JROW2)
    col2 = len(JCOL2)

    if (row1 != row2):
        return None
    
    count1 = len(AN1)
    count2 = len(AN2)
    count = count1 + count2

    row = row1
    col = col1 + col2

    JROW = JROW1.copy()
    JCOL = JCOL1.copy()
    JCOL.extend([i + count1 for i in JCOL2])

    AN = AN1.copy()
    AN.extend(AN2)

    NCOL = NCOL1.copy()
    NCOL.extend(plusArray(NCOL2.copy(), count1))
    
    NROW = NROW1.copy()
    NROW.extend(plusArray(NROW2.copy(), count1))
    for i in range(len(JROW)):
        if (JROW2[i] >=0 ):
            if (JROW1[i] == -1):
                JROW[i] = JROW2[i] + count1
            else:
                RLast = JROW[i] # first elem 
                while(NROW[RLast] > 0):
                    RLast = NROW[RLast]
                    
                NROW[RLast] = JROW2[i] + count1
                RLast = NROW[RLast]
                while (NROW[RLast] > 0):
                    RLast = NROW[RLast]
                NROW[RLast] = -JROW[i]

    
    
    
    return [AN, NROW, NCOL, JROW, JCOL]

def connectMatrix_Optim(mat1, mat2):
    AN1 = mat1[0]
    NROW1 = mat1[1]
    NCOL1 = mat1[2]
    LastRow1 = mat1[5]
    JROW1 = mat1[3]
    JCOL1 = mat1[4]
    row1 = len(JROW1)
    col1 = len(JCOL1)

    AN2 = mat2[0]
    NROW2 = mat2[1]
    NCOL2 = mat2[2]
    LastRow2 = mat2[5]
    JCOL2 = mat2[4]
    JROW2 = mat2[3]
    row2 = len(JROW2)
    col2 = len(JCOL2)

    if (row1 != row2):
        return None
    
    count1 = len(AN1)
    count2 = len(AN2)
    count = count1 + count2

    row = row1
    col = col1 + col2

    LastRow = LastRow1.copy()
    JCOL = JCOL1.copy()
    for i in JCOL2:
        if (i == -1):
            JCOL.append(i)
        else:
            JCOL.append(i + count1)
    #JCOL.extend([i + count1 for i in JCOL2 if i != -1])

    AN = AN1.copy()
    AN.extend(AN2)

    JROW = JROW1.copy()
    

    NCOL = NCOL1.copy()
    NCOL.extend(plusArray(NCOL2.copy(), count1))


    NROW = NROW1.copy()
    NROW.extend(plusArray(NROW2.copy(), count1))
    #array_print('Last 1', LastRow1)
    #array_print('Last 2', LastRow2)
    #array_print('NROW1', NROW1)
    #array_print('NROW2', NROW2)
    for i in range(len(LastRow)):
        # Hành i2 không trống
        if (LastRow2[i] >=0):
            # Hàng i1 trống
            if (LastRow1[i] == -1):
                LastRow[i] = LastRow2[i] + count1
            else:
                RLast1 = LastRow1[i] # last elem row 1
                RLast2 = LastRow2[i]
                
                Rfirst2 = -NROW2[RLast2]
                Rfirst1 = -NROW1[RLast1]
                
                NROW[RLast1] = Rfirst2 + count1
                NROW[RLast2 + count1] = -Rfirst1
                
                LastRow[i] = LastRow2[i] + count1
            #print(i, LastRow[i])
            JROW[i] = -NROW[LastRow[i]]

    
    
    return [AN, NROW, NCOL, JROW, JCOL, LastRow]


def matrix_print(A):
    print("Matrix")
    for i in A:
        array_print('', i)

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

def tester():
    for i in range(1, 50):
        row = randint(10, 100)
        col1 = randint(10, 100)
        p = randint(1, 9) / 10
        A1 = createMatrix(row, col1, p)
        A2 = fromNomalMatrix(A1)
        A3 = toNormalMatrix(A2)
        test = compareMatrix(A1, A3)
        if (test):
            print('Test Tranform ', test)
        else:
            print('*' * 1000)
            print('Test Tranform \t\t\t\t\t', test)
            break
    
    for i in range(1, 2):
        row = 5#randint(10, 100)
        col1 = 5#randint(10, 100)
        col2 = 5#randint(10, 100)
        p = 0.25#randint(1, 9) / 10
        A1 = createMatrix(row, col1, p)
        B1 = createMatrix(row, col2, p)
        print('Matrix A:')
        matrix_print(A1)
        print("Matrix B")
        matrix_print(B1)
        A2 = fromNomalMatrix(A1)
        B2 = fromNomalMatrix(B1)
        #print("Connecting....")
        C1 = connectNomalMatrix(A1, B1)
        print("Waiting Result:")
        matrix_print(C1)
        #print("Connecting....")
        print("Connect Resuly")
        C = connectMatrix_Optim(A2, B2)
        C2 = toNormalMatrix(C)
        matrix_print(C2)
        test = compareMatrix(C1, C2)
        if (test):
            print('Test Matrix Connect ', test)
        else:
            print('*' * 1000)
            print('Test Matrix Connect \t\t\t\t\t', test)
            break


fnArray = [connectMatrix, connectMatrix_Optim]
timerArray = [timer(fn) for fn in fnArray]

def graph_draw(p = 0.5, matrix_size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]):
    print("Matrix Creating...")
    p = p / 100
    MatrixA = [fromNomalMatrix(createMatrix(size, size, p)) for size in matrix_size]
    MatrixB = [fromNomalMatrix(createMatrix(size, size, p)) for size in matrix_size]
    rep = 10000
    len_size = len(matrix_size)
    len_Ar = len(fnArray)
    print("Timing...")    
    time_Ar = [[fn(MatrixA[i], MatrixB[i]) for i in range(len_size)] for fn in timerArray]
    print(time_Ar)
    label_Ar = ["алгоритм", "Оптимизированный алгоритм" ]
    format_Ar = ["bo-", "ro-"]
    print("Drawing...")
    
    for i in range(len_Ar):
        plt.plot(matrix_size, time_Ar[i], format_Ar[i], label = label_Ar[i])
    plt.xlabel("len")
    plt.ylabel("time(ms)")
    plt.legend(loc = "best")
    plt.show()

def main():
    #tester()
    graph_draw(1)


main()

                
            
            
