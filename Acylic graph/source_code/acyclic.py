'''
Find out if a graph is acyclic
Recursive implementation

execution instructions:
under ./Q1/source_code/ directory
> python acyclic.py <file_name>
example:
> python acyclic.py hw3-1.txt

Time complexity: O(V+E) due to DFS 
Space complexity: O(V) for marked[] list
'''

from sys import argv
from collections import defaultdict

# undirected graph using adjacency list
class Graph:
    def __init__(self, v):
        self.V = v
        # adjacency list using dictionary with vertices 
        # as keys and list of neighbors as values
        self.graph = defaultdict(list)
 
    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)
  
    # Recursive helper function that uses marked[] list and previously 
    # adjacent vertex to detect cycle in subgraph reachable from vertex v.
    def cyclic(self, v, marked, prev):
        marked[v]= True
        # iterate over all vertices
        for i in self.graph[v]:
            # if vertex not visited then recurse on it
            if  marked[i] == False :
                if self.cyclic(i, marked, v):
                    return True 
            # otherwise if adjacent vertex has been visited before and not 
            # previously adjacent to current vertex then there exists a cycle
            elif  i != prev:
                return True
        # no cycle exists if loop exits without returning
        return False
          
    # Check if graph is acyclic or not
    def acyclic(self):
        vertices = range(self.V)
        # marked list initialization
        marked = [False for v in vertices]
        # Iterate through all vertices in the worst case (acyclic)
        # this takes into account all components of the graph
        for v in vertices:
            if marked[v] == False:
                # if cyclic then return False
                if self.cyclic(v, marked, -1):
                    return False
        # otherwise acyclic
        return True


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
        # undirected weighted input
        if len(data[i])==3:
            v1, v2, weight = data[i]
        # undirected unweighted input
        elif len(data[i])==2:
            v1, v2 = data[i]
        g.addEdge(int(v1), int(v2))

    

if __name__ == '__main__':
    main()