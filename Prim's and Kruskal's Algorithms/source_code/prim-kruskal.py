'''
Prim's and Kruskal's Algorithm
In this implementation we use adjacency matrix for storing the graph 
in case of Prim's algorithm & edge list in case of Kruskal's algorithm

execution instructions: 
under ./Q1/source_code/ directory
> python prim-kruskal.py <filename> 
example:
> python prim-kruskal.py HW3-1.txt

Note: Execution times calculated for Prim's and Kruskal's algorithm are average over
      numIterations (5) passes. Change numIterations to whatever to find a better average.

'''
from sys import argv
import sys
import time

class GraphAdjMatrix:
    def __init__(self, v):
        self.V = v
        # adjacency matrix initialized to all infinity
        self.graph = [[float('inf') for i in range(v)] for j in range(v)]
        # integer for counting traversal steps
        # self.check = 0
 
    def addEdge(self, v1, v2, w):
        self.graph[v1][v2] = w
        self.graph[v2][v1] = w

    # returns index of the next vertex closest 
    # to the source using the dist list
    def nextVertex(self, dist, closed):
        # set min to infinity
        min = float('inf')
        # for each non-closed vertex in the graph check if 
        # their corresponding dist[] value is less than min
        for v in range(self.V):
            if dist[v] < min  and not closed[v]:
                min = dist[v]
                idx = v
        # return index of vertex with minimum vertex
        return idx
    
    def prim(self):
        dist = [float('inf') for i in range(self.V)]
        mst = [None for i in range(self.V)]
        closed = [False for i in range(self.V)]
        # vertex 0 picked first
        dist[0] = 0
        mst[0] = -1 
        # iterate over all vertices
        for _ in range(self.V):
            # find the next vertex with the minimum distance
            # from the list of unprocessed vertices
            u = self.nextVertex(dist, closed)
            # mark vertex as closed (not to be worked upon anymore)
            closed[u] = True
            # for all adjacent vertices update distances 
            # if incoming dist is less than curr dist
            # then add to mst
            for v in range(self.V):
                if self.graph[u][v] < float('inf') and not closed[v] and dist[v] > self.graph[u][v]:
                        dist[v] = self.graph[u][v]
                        mst[v] = u

        return mst


class GraphEdgeList:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # typical recursive union find()
    def find(self, mst, i):
        if mst[i] == i:
            return i
        return self.find(mst, mst[i])
 
    # union of x and y sets by rank
    def union(self, mst, rank, u, v):
        rootU = self.find(mst, u)
        rootV = self.find(mst, v)
 
        # set root of lower rank tree to that of higher rank tree
        if rank[rootU] < rank[rootV]: mst[rootU] = rootV
        elif rank[rootV] < rank[rootU]: mst[rootV] = rootU
        # otherwise if equal, set one as root and increment its rank by 1
        else:
            mst[rootV] = rootU
            rank[rootU] += 1
 
    # Kruskal's algorithm using union find
    def kruskal(self):
        mst, prev, rank = [], [], []
        i, e =0, 0
        # sort by edge weights
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # Create V subsets with single elements
        for v in range(self.V):
            prev.append(v)
            rank.append(0)
        # iterate for V-1 edges i.e. the # edges in the resultant mst
        while e < self.V - 1:
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i += 1
            x = self.find(prev, u)
            y = self.find(prev, v)
            # if x == y then cycle otherwise add edge 
            # to mst and continue on to next edge
            if x != y:
                e += 1
                mst.append([u, v, w])
                self.union(prev, rank, x, y)

        return mst


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
    gPrim = GraphAdjMatrix(V)
    gKruskal = GraphEdgeList(V)

    for i in range(2,len(data)):
        v1, v2, weight = data[i]
        gPrim.addEdge(int(v1), int(v2), float(weight))
        gKruskal.addEdge(int(v1), int(v2), float(weight))

    numIterations = 5
    start_time = time.time()
    
    for _ in range(numIterations): 
        gPrim.prim()

    end_time = time.time()
    avg_time = (end_time - start_time)/numIterations*1000
    print ("Exec time for Prim's Algorithm = %.2f" % avg_time, "ms")

    # print ("MST:")
    # for i in range(1, g.V):
    #     print (mst[i], "<->", i, "\t:", g.graph[i][mst[i]])
    
    start_time = time.time() 

    for _ in range(numIterations): 
        mst = gKruskal.kruskal()
    
    # minCost = 0
    # print ("MST: ")
    # for u, v, weight in mst:
    #     minCost += weight
    #     print(u, " <-> ", v, ":\t", weight))
    # print ("Minimum cost of MST (Kruskal) = ", minCost)

    end_time = time.time()
    avg_time = (end_time - start_time)/numIterations*1000
    print ("Exec time for Kruskal's Algorithm = %.2f" % avg_time, "ms")
    


if __name__ == '__main__':
    main()
