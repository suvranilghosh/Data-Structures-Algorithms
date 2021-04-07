'''
Quicksort using Median of 3 values as Pivot
***execution instructions***
>cd /Q5/source_code/
>python quicksort.py <filename>
example cmd line: 
>python quicksort.py data1.16384
add custom data files under the '/Q5/data' directory 
'''

import time
from sys import argv

# cutoff between insertion sort and quicksort
# for input of size > cutoff, do quicksort
# otherwise do insertion sort
cutOff = 200

# simple caller function for quicksort
def quickSort(arr):
    _quickSort(arr, 0, len(arr))


# basic insertion Sort
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 


# finds median of 3 values
# sorts a list of the 3 values
# returns middle value aka median
def median(a, b, c):
    return sorted([a,b,c])[1]


def partition(arr, lo, hi):
    # left, right and middle elements on arr[lo:hi]
    left = arr[lo]
    right = arr[hi-1]
    mid = arr[(hi+lo)//2]

    # set the median of left, right and mid to be the pivot
    pivot = median(left, right, mid)

    # swap pivot and left element
    arr[arr.index(pivot)] = left
    arr[lo] = pivot

    # bring all values that are to the right of and 
    # less than the pivot to the left of it
    i = lo + 1
    for j in range(lo + 1, hi):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    # adjust previous pivot position
    temp = arr[lo]
    arr[lo] = arr[i-1]
    arr[i-1] = temp
    return i - 1 


# basic recursive quicksort
# partition around pivot which in this case is the 
# median of left right and middle values
# recursive quicksort left and then right partitions 
def _quickSort(arr, lo, hi):
    if lo < hi:
        pi = partition(arr, lo, hi)
        _quickSort(arr, lo, pi)
        _quickSort(arr, pi + 1, hi)


def main(): 
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("../data/"+argv[1], 'r')
    lines = f.readlines()
    arr = [int(line) for line in lines]

    # arr = list(random.randint(cutOff, size=(cutOff)))
    n = len(arr)

    if n <= cutOff:
        #insertion sort
        print("**Insertion Sort**")
        start_time = time.time() 
        insertionSort(arr)
        end_time = time.time()
    else:
        #quicksort
        print("**Quicksort**")
        start_time = time.time() 
        quickSort(arr)
        end_time = time.time()

    time_taken = (end_time - start_time)*1000
    print ("Exec time = %.2f" % time_taken, "ms")


if __name__ == '__main__':
    main()

