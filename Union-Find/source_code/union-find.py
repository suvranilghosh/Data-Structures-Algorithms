'''
Quick Find, Quick Union, Weighted Quick Union
***execution instructions*** 
>cd /Q2/source_code/
>python union-find.py <filename>
example cmd line: 
>python union-find.py 8192pair.txt
add custom data files under the '/Q2/data' directory 
'''

import time
from sys import argv
# change according to range of datasets
N = 8192 

class QuickFind(object):
    id = []
    def __init__(self, N):
        # assign a list of N integers to their corresponding
        # indices id[0]->0, id[1]->1, id[2]->2, etc.
        self.id = [i for i in range(N)]

    # find(): is the pair connected?
    def Connected(self, p, q):  
        return self.id[p]==self.id[q]
    
    # connect pairs
    def Union(self, p, q): 
        # if p and q are not connected already, connect them
        if(self.Connected(p,q) == False):
            pid = self.id[p]
            qid = self.id[q]
            for i in range(len(self.id)):
                if self.id[i] == pid:
                    self.id[i] = qid
            #print("Connected:",p,"&",q)

# Quick Union and Quick Union Weighted
class QuickUnion(object):
    id = []
    sz = []
    def __init__(self, N):
        # assign a list of N integers to their corresponding
        # indices id[0]->0, id[1]->1, id[2]->2, etc.
        self.id = [i for i in range(N)]
        # list of size N with all entries = 1 for storing "weights"
        self.sz = [1 for i in range(N)]

    # find the root of a element id[i]
    def Root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    # is the pair connected?
    def Connected(self, p, q):
        return self.Root(p) == self.Root(q)

    # connect pairs by assigning root of q to be the root of p
    def Union(self, p, q):
        if(self.Connected(p,q) == False):
            i = self.Root(p)
            j = self.Root(p)
            self.id[i] = j
            #print("Connected:",p,"&",q)
    
    # connect pairs after comparing weights
    def UnionWeighted(self, p, q):
        if(self.Connected(p,q) == False):
            i = self.Root(p)
            j = self.Root(p)
            if self.sz[i] < self.sz[j]:
                self.id[i] = j
                self.sz[j] += self.sz[i]
            else:
                self.id[j] = i
                self.sz[i] += self.sz[j]
            #print("Connected:",p,"&",q)

def main(): 
    
    obj1 = QuickFind(N)
    obj2 = QuickUnion(N)
    
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("../data/"+argv[1], 'r')
    lines = f.readlines()

    # Quick Find
    total_time=0
    for i in range(len(lines)):
        p,q= lines[i].split()
        p,q=[int(p),int(q)]
        start_time = time.time()
        obj1.Union(p,q)
        end_time = time.time()
        total_time+=end_time - start_time
        #print(p,q)
        
    total_time*=1000
    print ("Exec time for  QuickFind = %.3f " % total_time, "ms")

    # Quick Union
    total_time=0
    for i in range(len(lines)):
        p,q= lines[i].split()
        p,q=[int(p),int(q)]
        start_time = time.time()
        obj2.Union(p,q)
        end_time = time.time()
        total_time += (end_time - start_time)
        #print(p,q)

    total_time*=1000000
    print ("Exec time for  QuickUnion =  %.3f " % total_time, "us")

    # Quick Union Weighted
    total_time=0
    for i in range(len(lines)):
        p,q= lines[i].split()
        p,q=[int(p),int(q)]
        start_time = time.time()
        obj2.UnionWeighted(p,q)
        end_time = time.time()
        total_time += (end_time - start_time)
        #print(p,q)

    total_time*=1000000
    print ("Exec time for  QuickUnionWeighted = %.3f " % total_time, "us")

if __name__ == '__main__':
    main()          