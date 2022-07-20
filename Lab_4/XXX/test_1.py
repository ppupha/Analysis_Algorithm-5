from multiprocessing import Pool
from timeit import default_timer as timer
import defs
#Create sizes for 3 arrays. 
sizes = [ 10**6 * 50 for i in range(0,3)] #Size of each array is 10 here.
#Applying the function sequentially
tic = timer()
[defs.createandsort(size) for size in sizes]
tac = timer()
print("time for sequential sorting: ", tac-tic)
#Using multiprocessing
if __name__ == "__main__":
    pool = Pool(processes=3)
    tic = timer()
    pool.map(defs.createandsort,sizes)
    tac = timer()
    print("time for parallel sorting: ",tac-tic)
