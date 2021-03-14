import time
import os
import multiprocessing


def Square(no):
    return no*no

def ParallelProcessing():

    start = time.time()

    print("Parallel Processing")

    arr = range(100)

    ret = []

    pobj = multiprocessing.Pool()

    ret = pobj.map(Square , arr)

    end = time.time()

    print("Time required for Parallel execution",end-start)




def SerialProcessing():

    start = time.time()

    print("Serial Processing")

    arr = range(100)

    ret = []

    for i in arr:
        ret.append(Square(i))


    end = time.time()

    print("Time required for serial execution",end-start)



def main():

    SerialProcessing()
    ParallelProcessing()

if __name__ == '__main__':
    main()