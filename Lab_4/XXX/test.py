import multiprocessing
import time

def square_list(result): 
    """ 
    function to square a given list 
    """
    # append squares of mylist to result array 
    for idx in range(len(result)):
        for i in range(100):
            result[-idx] = idx
        c = [i for i in range(10000)]
        for i in range(10000):
            a = c[i] * c[i] * 9999 / 9999
        #time.sleep(0.1)

def squarelist(result, i, j): 
    """ 
    function to square a given list 
    """
    # append squares of mylist to result array 
    for idx in range(i, j):
        for i in range(100):
            result[idx] = idx
        c = [i for i in range(10000)]
        for i in range(10000):
            a = c[i] * c[i] * 9999 / 9999
        #time.sleep(0.1)
        
def test1(result):
    # creating new process
    l = 10000
    n = 4
    arr = [i for i in range(0, l+1, l // n)]#[multiprocessing.Value('i', i) for i in range(0, l+1, l // n)]
    arr[n] = l
    p_arr = []

    for i in range(n):
        p = multiprocessing.Process(target=squarelist, args=(result, arr[i], arr[i+1]))
        p.start()
        p_arr.append(p)
    #p1 = multiprocessing.Process(target=squarelist, args=(result, 0, l // 2))
    #p2 = multiprocessing.Process(target=squarelist, args=(result, l // 2, l))
    #p3 = multiprocessing.Process(target=squarelist, args=(result, x * y // 2, x * y))
    #p4 = multiprocessing.Process(target=squarelist, args=(result, x * y // 2, x * y))
    #p_arr = [p1, p2]

    for p in p_arr:
        p.join()
        
def test2(result):
    square_list(result)

if __name__ == "__main__":
    
    result = [0 for i in range(10000)]
    start = time.time()
    test2(result)
    end = time.time()
    print('Time 1 process: ', end - start)
    #print(result)
    result = multiprocessing.Array('i', 10000)
    start = time.time()
    test1(result)
    end = time.time()
    print('Time: MultiProcess ', end - start)
    #print(result[:])



   
