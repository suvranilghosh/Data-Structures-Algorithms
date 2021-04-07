'''
3-Sum - Naive and Sophisticated
***execution instructions*** 
> cd Q1/source_code/
> python 3sum.py <filename>
example cmd line: 
> python 3sum.py 8int.txt
add custom data files under the '/Q1/data' directory 
'''

import time
from sys import argv

# recursive binary search for x in arr[lo:hi]
def binarysearch(arr, lo, hi, x):
    if hi>=lo:
        mid = (hi+lo)//2
        if arr[mid]==x: #value found
            return True
        elif x<arr[mid]:    #if key less than middle element
            return binarysearch(arr, lo, mid-1, x) #search left
        else:
            return binarysearch(arr, mid+1, hi, x) #search right
    else:
        return False

# 3 sum algorithm - naive version
# check if sum of each 3-combination is equal to 0
def naive3sum(data):
    count = 0
   
    for i in range(len(data)-2):
        for j in range(i+1, len(data)-1):
            for k in range(j+1, len(data)):
                if(data[i]+data[j]+data[k]==0): 
                    count+=1
    
    return count

# 3 sum algorithm - sophisticated version
# select pairs and binary search of negative of sum of 
# pair values in the rest of the list
def sophisticated3sum(data):
    count = 0
    data.sort() #nlogn
    
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if binarysearch(data, j+1, len(data)-1, -(data[i]+data[j]))==True:
                count+=1
    
    return count

def main(): 
    # open data file in read mode
    # read each line of the file
    # convert line strings to integer and store in data list
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("../data/"+argv[1], 'r')
    lines = f.readlines()
    data = [int(line) for line in lines]
    
    # binary search test
    # a = binarysearch(data, 0, len(data)-1, 69)
    # print(a)

    start_time = time.time() 
    count1 = naive3sum(data)
    end_time = time.time()
    
    print ("Exec time for \"naive\" 3 sum = %.2f" % (end_time - start_time), "seconds")

    # start_time = time.time() 
    # count2 = sophisticated3sum(data)
    # end_time = time.time()

    # print ("Exec time for \"sophisticated\" 3 sum = %.2f" % (end_time - start_time), "seconds")    
    # # print(count1)
    # # print(count2)
    # if count1 == count2:
    #     print("Number of 3 sums = ", count1)
    # else: print("Computation incorrect!")

if __name__ == '__main__':
    main()