'''
# Dijkstra's algorithm implementation

# execution instructions:
# under ./Q6/source_code/ directory
# > python dijkstra.py <file_name>
# example:
# > python dijkstra.py 4a.txt

Note: Topological sorting not performed. 
      Manually input source vertex (line 88).
'''

from sys import argv
import sys

class Graph:
    def __init__(self, v):
        self.V = v
        # adjacency matrix initialized to all zeroes
        self.graph = [[float('inf') for i in range(v)] for j in range(v)]
        # integer for counting traversal steps
        # self.check = 0
 
    def addEdge(self, v1, v2, w):
        self.graph[v1][v2] = w

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

    def dijkstra(self, s):
        # initialize list for storing shortest distances
        # dist[i] denotes distance of vertex i from vertex s
        dist = [float('inf') for i in range(self.V)]
        # distance from s to s is 0
        dist[s] = 0
        # boolean list to store closed vertices
        closed = [False for i in range(self.V)]

        for _ in range(self.V):
            # find the next vertex with the minimum distance from the source
            v = self.nextVertex(dist, closed)
            # close the vertex and then work on it 
            closed[v] = True
            for u in range(self.V):
                # if the current distance is greater than the 
                # incoming distance, assign the latter to dist[u]
                if self.graph[v][u] < float('inf') and not closed[u] and dist[u] > dist[v] + self.graph[v][u]: 
                    dist[u] = dist[v] + self.graph[v][u]
        return dist

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
        g.addEdge(int(v1), int(v2), float(weight))

    # ***********************************
    # CHANGE START VALUE OF DIJKSTRA HERE
    # ***********************************
    result = g.dijkstra(5)
    print(result)


if __name__ == '__main__':
    main()

