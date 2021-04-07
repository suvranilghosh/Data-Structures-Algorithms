'''
Kendall Tau distance between two rankings - one of them being pre-sorted
***execution instructions***
>cd /Q3/source_code/
>python kendall_tay.py <input_size>
example cmd line: 
>python kendall_tay.py 8192
add custom data files under the '/Q3/data' directory
make sure the datafiles are in pairs:
data0.x and data1.x
x = file_length for eg: 1024, 4096, 2048 etc.
data0.x has to be sorted in ascending order
see main() function for more details about custom data input
'''

import time
from sys import argv

#constructor-ish function for easier call from main
def mergeSort(list, n):
    temp = [0]*n
    return _mergeSort(list, temp, 0, n-1)
 
 
def _mergeSort(list, temp, lo, hi):
    numInversions = 0
    if lo < hi:
        mid = (lo + hi)//2
        # calculate number of inversions in lo half
        numInversions += _mergeSort(list, temp, lo, mid)
        # calculate number of inversions in hi half
        numInversions += _mergeSort(list, temp, mid + 1, hi)
        # calculate number of inversions while merging
        numInversions += merge(list, temp, lo, mid, hi)
    return numInversions


def merge(list, temp, lo, mid, hi):
    i = lo
    j = mid + 1 
    k = lo 
    numInversions = 0
    # iterating through left and right sublists
    while i <= mid and j <= hi:
        # if entry in the left sublist < entry in the right sublist 
        # => no inversions otherwise there is an inversion
        if list[i] <= list[j]:
            temp[k] = list[i]
            k += 1
            i += 1
        else:
            temp[k] = list[j]
            # all entries to the right of element in the left sublist also going to be greater
            # than list [j] hence we count for those too and increment numInversions accordingly
            numInversions += (mid-i + 1)
            k += 1
            j += 1
    # for the elements remaining in the left and right sublists
    while i <= mid:
        temp[k] = list[i]
        k += 1
        i += 1
    while j <= hi:
        temp[k] = list[j]
        k += 1
        j += 1
    # copy back into original list
    for x in range(lo, hi + 1):
        list[x] = temp[x]
         
    return numInversions

# Given two rankings data0.x and data1.x, if data0 is sorted, then
# the problem of computing the Kendall tau distance reduces to computing 
# the number of inversions in data1.x which is what we are doing here
# Source: Wikipedia

def main(): 
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    # reading data1.x files, x being the cmd line input
    # if different set of data change string under open(...) and cmd line input accordingly 
    f = open("../data/data1."+argv[1], 'r') 
    lines = f.readlines()
    list = [int(line) for line in lines]
    
    n = len(list)

    start_time = time.time() 
    numInversions = mergeSort(list, n)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000

    kendallTau = numInversions/(n*(n-1))
    print("Kendall's Tau distance between data0."+argv[1]+" & data1."+argv[1]+" :%.3f " % kendallTau)
    print ("Exec time = %.2f" % time_taken, "ms")



if __name__ == '__main__':
    main()