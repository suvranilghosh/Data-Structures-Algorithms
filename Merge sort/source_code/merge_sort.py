# Recursive and Bottum-Up Mergesort
# ***execution instructions***
# >cd /Q4/source_code/
# >python merge_sort.py <filename>
# example cmd line: 
# >python merge_sort.py data1.16384
# add custom data files under the '/Q4/data' directory 

import time, math
from sys import argv


#recursive mergesort
def mergeSort_recursive(arr, count):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
       
        #recursive mergesort call on each half
        count = mergeSort_recursive(left, count)
        count = mergeSort_recursive(right, count)
        i = 0
        j = 0
        k = 0

        # comparing and partial merging of left and right sublists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            count += 1

        # comparing and merging remaining values from left and right sublists
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
    return count
    

#merges arr[lo:mid] and arr[mid+1:hi]
def merge(arr, temp, lo, mid, hi, count):
    i = k = lo
    j = mid + 1
    while i <=mid and j <= hi:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
        count += 1
    #merge remaining in case of unequal splits
    while i < len(arr) and i <= mid: 
        temp [k] = arr[i]
        i += 1
        k += 1
    for i in range(lo, hi+1):
        arr[i] = temp[i]
    
    return count

        
#bottom-up/iterative/non-recursive mergesort
def mergeSort_bottomup(arr, count):
    lo = 0
    hi = len(arr) - 1
    # temp = []
    # for i in range(lo, hi+1):
    #     temp[i] = arr[i]  
    temp = arr.copy()
    block_size = 1
    while block_size <= hi - lo:
        for i in range(lo, hi, 2*block_size):
            low = i
            mid = i + block_size - 1
            high = min(hi, i + 2*block_size - 1)
            count = merge (arr, temp, low, mid, high, count)
        block_size *= 2

    return count

def main(): 
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("../data/"+argv[1], 'r')
    lines = f.readlines()
    arr = [int(line) for line in lines]
    n = len(arr)

    count1 = 0
    count2 = 0

    start_time = time.time() 
    count1 = mergeSort_recursive(arr, count1)
    end_time = time.time()

    time_taken = (end_time - start_time)*1000
    # print(arr)
    
    print ("***Recursive mergesort***")
    print ("Number of comparisons made: ", count1)    #int(n*math.log(n,2))
    print ("Execution time = %.2f" % time_taken, "ms")

    arr = [int(line) for line in lines]
    start_time = time.time() 
    count2 = mergeSort_bottomup(arr, count2)
    end_time = time.time()

    time_taken = (end_time - start_time)*1000
    # print(arr)
    print ("***Bottum-up mergesort***")
    print ("Number of comparisons made: ", count2)
    print ("Exec time = %.2f" % time_taken, "ms")
    
   
if __name__ == '__main__':
    main()