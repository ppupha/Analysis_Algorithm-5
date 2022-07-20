
import time
import matplotlib.pyplot as plt
import random, string
 
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def update_file(filename, title, time_arr):
    f = open(filename, "w+")
    f.write("{}\n".format(title))

    '''len = len(title_arr)
    for i in range(len-1):
        f.write(title_arr[i], end = ";")
    fwrite(title_arr[len - 1])'''

    n = len(time_arr)
    m = len(time_arr[0])

    for j in range(m):
        for i in range(n - 1):
            f.write("{};".format(round(time_arr[i][j], 7)))
        f.write("{}\n".format(round(time_arr[n-1][j], 7)))

    f.close()
    

def levenshtein_recursive(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if (len1 == 0):
        return len2
    if (len2 == 0):
        return len1
    
    is_equal = 1
    if (str1[len1 - 1] == str2[len2 - 1]):
        is_equal = 0

    return min(levenshtein_recursive(str1, str2[0 : len2 - 1]) + 1,
               levenshtein_recursive(str1[0 : len1 - 1], str2) + 1,
               levenshtein_recursive(str1[0:len1 - 1], str2[0:len2 - 1]) + is_equal)

def mat_print(mat):
    for i in mat:
        print(i)

def levenshtein_recursive_table(str1, str2, is_print = 0):
    res = levenshtein_recursive_tab(str1, str2)
    if is_print:
        mat_print(levenshtein_recursive_tab.mat)

    delattr(levenshtein_recursive_tab, "mat")
    return res


def levenshtein_recursive_tab(str1, str2):
    fn = levenshtein_recursive_tab
    len1 = len(str1)
    len2 = len(str2)
    if not hasattr(fn, "mat"):
        fn.mat = [[-1 for i in range(len2 + 1)] for i in range(len1 + 1)]

    if (len1 == 0):
        fn.mat[len1][len2] = len2
        return len2
    if (len2 == 0):
        fn.mat[len1][len2] = len1
        return len1

    f1, f2, f3 = 0, 0, 0
    is_equal = 1
    
    if (str1[len1 - 1] == str2[len2 - 1]):
        is_equal = 0
        
    if (fn.mat[len1][len2 - 1] == -1):
        f1 = fn(str1, str2[0 : len2 - 1]) + 1
    else:
        f1 = fn.mat[len1][len2 - 1] + 1
        
    if (fn.mat[len1 - 1][len2] == -1):
        f2 = fn(str1[0 : len1 - 1], str2) + 1
    else:
        f2 = fn.mat[len1 - 1][len2] + 1
            
    if (fn.mat[len1 - 1][len2 - 1] == -1):
        f3 = fn(str1[0:len1 - 1], str2[0:len2 - 1]) + is_equal
    else:
        f3 = fn.mat[len1 - 1][len2 - 1] + is_equal

    minn = min(f1, f2, f3)
    fn.mat[len1][len2] = minn
    return minn

def levenshtein(str1, str2, is_print = 0):

    len1 = len(str1)
    len2 = len(str2)
    
    C = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    for i in range(0, len2 + 1):
        C[0][i] = i

    for i in range(0, len1 + 1):
        C[i][0] = i

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if (str1[i - 1] == str2[j - 1]):
                equal = 0
            else:
                equal = 1
                
            C[i][j] = min(C[i][j-1] + 1,
                          C[i-1][j] + 1,
                          C[i-1][j-1] + equal)
    if (is_print):
        matrix_print(str1, str2, C)
    return C[len1][len2]
                          

def damerau_levenshtein(str1, str2, is_print = 0):
    len1 = len(str1)
    len2 = len(str2)
    
    C = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    for i in range(0, len2 + 1):
        C[0][i] = i

    for i in range(0, len1 + 1):
        C[i][0] = i

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if (str1[i - 1] == str2[j - 1]):
                equal = 0
            else:
                equal = 1
                
            C[i][j] = min(C[i][j-1] + 1,
                          C[i-1][j] + 1,
                          C[i-1][j-1] + equal)
            
            if (i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]):
                C[i][j] = min(C[i][j], C[i-2][j - 2] + 1)

    if (is_print):
        matrix_print(str1, str2, C)
    return C[len1][len2]

        
def matrix_print(s1, s2, mat):
    str1 = " " + s1
    str2 = " " + s2
    
    len1 = len(str1)
    len2 = len(str2)
    space = 1
    print("{:-^5}".format(" "), end = "")

    for i in range(len2):
        print("{:^5}".format(str2[i]), end = "")
    print()
    
    for i in range(len1):
        print("-" * (len2 + 1) * 5)
        print("{:^5}".format(str1[i]), end = "")
        for j in range(len2):
            print("{:^5}".format(mat[i][j]), end = "")
        print()
        

def timer(fn, rep = 10):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        for i in range(rep):
            result = fn(*args, **kwargs)
        end_time = time.time()
        #print('total run-time of {}: {} ms'.format(fn.__name__, (end_time - start_time) * 1000 / rep))
        return (end_time - start_time) * 1000 / rep
    return wrapper

damerau_levenshtein_timer = timer(damerau_levenshtein)
levenshtein_timer = timer(levenshtein)
levenshtein_recursive_timer = timer(levenshtein_recursive)
levenshtein_recursive_table_timer = timer(levenshtein_recursive_table)

def tester(str1, str2, result_levenshtein, result_damerau_levenshtein):
    
    res = levenshtein(str1, str2)
    if (res != result_levenshtein):
        print("Test levenshtein Fail")

    res = levenshtein_recursive(str1, str2)
    if (res != result_levenshtein):
        print("Test levenshtein_recursive Fail")

    res = levenshtein_recursive_table(str1, str2)
    if (res != result_levenshtein):
        print("Test levenshtein_recursive_table Fail {} {} {} {}".format(str1, str2, res, result_levenshtein))

    res = damerau_levenshtein(str1, str2)
    if (res != result_damerau_levenshtein):
        print("Test damerau_levenshtein Fail")

def func_test():

    print("Start Testing.......")
    tester("", "", 0, 0)
    tester("a", "a", 0, 0)
    tester("a", "", 1, 1)
    tester("a", "b", 1, 1)
    tester("abc", "acb", 2, 1)
    tester("1234", "567", 4, 4)
    tester("human", "cat", 4, 4)

    print("Test Finished")

def draw():
    print(".....")
    arr_str_len = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,]#200, 300]
    arr_str_len = [0, 50, 100, 200, 300]
    arr_str1 = [randomword(i) for i in arr_str_len]
    arr_str2 = [randomword(i) for i in arr_str_len]
    time_damerau_levenshtein = [damerau_levenshtein_timer(arr_str1[i], arr_str2[i])
                                for i in range(len(arr_str_len))]

    time_levenshtein = [levenshtein_timer(arr_str1[i], arr_str2[i])
                                for i in range(len(arr_str_len))]

    

    #time_levenshtein_recursive = [levenshtein_recursive_timer(arr_str1[i], arr_str2[i]) for i in range(len(arr_str_len))]
    time_levenshtein_recursive_table = [levenshtein_recursive_table_timer(arr_str1[i], arr_str2[i]) for i in range(len(arr_str_len))]

    print(time_levenshtein)
    print(time_damerau_levenshtein)
    print(time_levenshtein_recursive_table)
    print("in")
    update_file("text.txt", "Size;Leven;Damerau;Damerautable",[arr_str_len, time_levenshtein, time_damerau_levenshtein, time_levenshtein_recursive_table])
    print("out")
    plt.plot(arr_str_len, time_damerau_levenshtein, "bo-", label = "damerau_levenshtein")
    plt.plot(arr_str_len, time_levenshtein, "ro-", label = "levenshtein")
    
    plt.plot(arr_str_len, time_levenshtein_recursive_table, "go-", label = "levenshtein_recursive_table")
    #plt.plot(arr_str_len, time_damerau_levenshtein, "bo-", label = "levenshtein_recursive")
    plt.xlabel("len")
    plt.ylabel("time(ms)")
    plt.legend(loc = "best")
    plt.show()

    #print(time_damerau_levenshtein)
    #print(time_levenshtein)

def func_graph(fn):
    arr_str_len = [1, 2, 3, 4, 5, 6, 7, 8]# 200, 300]
    arr_str1 = [randomword(i) for i in arr_str_len]
    arr_str2 = [randomword(i) for i in arr_str_len]
    fn_timer = timer(fn)
    time_fn = [fn_timer(arr_str1[i], arr_str2[i])
                                for i in range(len(arr_str_len))]

    print(time_fn)
    plt.plot(arr_str_len, time_fn, "go-", label = fn.__name__)
    plt.xlabel("len")
    plt.ylabel("time(ms)")
    plt.legend(loc = "best")
    plt.show()



    

def main():
    str1 = input("Input First String: ")
    str2 = input("Input Second String: ")

    res = damerau_levenshtein(str1, str2, 1)
    print("Result (damerau_levenshtein) is: {:10}".format(res))

    res = levenshtein(str1, str2, 1)
    print("Result(levenshtein) is: {:10}".format(res))

    res = levenshtein_recursive(str1, str2)
    print("Result(levenshtein_recursive) is: {:10}".format(res))

    res = levenshtein_recursive_table(str1, str2, 1)
    print("Result(levenshtein_recursive_table) is: {:10}".format(res))






#main()
#func_test()
draw()

#func_graph(levenshtein_recursive)
#func_graph(levenshtein_recursive_table)

#func_graph(levenshtein)


