'''
BFS and DFS on undirected weighted
API used: Adjacency list with neighbors 
and their respective weights stored in tuples

execution instructions: 
under ./Q3/source_code/ directory
> python bdfs.py <file_name>
example:
> python bdfs.py NYC.txt

To change starting value for DFS and BFS, check driver 
Note: recursion limit problems for DFS on NYC.txt

'''
from collections import defaultdict
from sys import argv
import sys

class Graph:
    def __init__(self, u):
        self.V = u
        # adjacency list using dictionary with vertices 
        # as keys and list of neighbors as values
        self.graph = defaultdict(list)
        # integer for counting traversal steps
        self.check = 0
 
    def addEdge(self, v1, v2, w):
        self.graph[v1].append((v2,w))

    def DFSHelper(self, v, marked, stack):
        # 
        # mark starting vertex as visited
        marked[v] = True
        # add starting vertex to stack
        stack.append(v)
        while (stack):
            # pop vertex from stack
            v = stack.pop()

            # mark popped vertex as visited if not already
            if marked[v] == False:
                marked[v] = True
                self.check += 1
                # print (v, end='-')

            # traverse through neighbors of popped vertex
            # and add to stack for doing DFS on each
            for adj in self.graph[v]:
                if marked[adj[0]] == False:
                    stack.append(adj[0])

    def DFS(self, v):
        marked = [False for vertex in range(self.V)]
        stack = []
        self.DFSHelper(v, marked, stack)
        
        
    def BFSHelper(self, v, marked, queue):
        # mark starting vertex as visited
        marked[v] = True
        # queue it
        queue.append(v)
        # while queue is not empty
        while queue:
            # dequeue vertex from queue
            v = queue.pop(0)
            # print(v, end = '-')
            # visit and queue every neighbor of v
            for adj in self.graph[v]:
                # if neighbor not visited, add it 
                # to queue and mark it as visited
                if marked[adj[0]] == False:
                    queue.append(adj[0])
                    marked[adj[0]] = True

    def BFS(self, v):
        marked = [False for vertex in range(self.V)]
        queue = []
        self.BFSHelper(v, marked, queue)


def main(): 
    # open data file in read mode
    # read each line of the file
    # convert line strings to integer lists and store in data list
    
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("../data/"+argv[1], 'r')
    lines = f.readlines()
    data = [line.split() for line in lines]
    
    V = int(data[0][0]) 
    E = int(data[1][0])

    # Create a graph from the input
    g = Graph(V)

    for i in range(2,len(data)):
        v1, v2, weight = data[i]
        g.addEdge(int(v1), int(v2), int(weight))

    sys.setrecursionlimit(2000000000)
    
    # ******************************
    # CHANGE START VALUE OF BFS HERE
    # ******************************
    # BFS starting from 1
    g.BFS(1)


    # ******************************
    # CHANGE START VALUE OF DFS HERE
    # ******************************
    # DFS starting from 1
    g.DFS(1)
    # print (g.check, "vertices traversed in DFS")


if __name__ == '__main__':
    main()

