'''
Average Path Length of in a tree
From N random insertions and N sorted insertions

execution instructions: 
under ./Q1/source_code/ directory
> python avgPathLength.py <N>(optional) 
N defaults to 2462 if no argument is provided
example:
> python avgPathLength.py 1024

Note: Max value of N is 2462 since we are limited by Python's recursion depth which is set to 
2 Million in this case in line 84. If larger values of N are needed for test cases, please increase
the recursion depth accordingly
'''
import sys
import time
import random
from sys import argv

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
    def insertNode(self, node):
        # values greater than parent goes right and less ones go left
        # done recursively if the immediate child is not empty
        if node.key >= self.key: 
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insertNode(node)
        else:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insertNode(node)
        
class Tree:
    def __init__(self):
        self.root = None
 
    def add(self, key):
        new_node = Node(key)
        # if root of tree/subtree is empty add node to root
        if self.root is None:
            self.root = new_node
        # else use insertNode function
        else:
            self.root.insertNode(new_node)

    def depth(self, node, depth, sum):
        # recursively find sum of depths of all nodes in a tree
        if node is None:
            return sum
        # find sum of depths of all nodes in left subtree
        sum = self.depth(node.left, depth + 1, sum)
        # find sum of depths of all nodes in right subtree
        sum = self.depth(node.right, depth + 1, sum)
        # add the sums of left and right subtrees and return
        sum += depth
        return sum

    def pathLength(self, sum):
        # returns total path length
        sum = self.depth(self.root, 0, sum)
        return sum
        
def main(): 
    bstRand = Tree()
    bstSorted = Tree()
    
    if len(argv)>1 and int(argv[1])>0: N = int(argv[1])
    else: N = 2426
    print("Proceeding with N =", N,"...")

    # ***************************
    # CHANGE RECURSION DEPTH HERE
    # ***************************
    sys.setrecursionlimit(2000000)
    
    for num in range(N):
        bstSorted.add(num)
        bstRand.add(random.randint(1,N))

    # calculate avg path length
    sum = 0
    avgPathLength_rand = bstRand.pathLength(sum)/N
    sum = 0
    avgPathLength_sorted = bstSorted.pathLength(sum)/N

    print("Average Path Length of tree with N random insertions = %.1f" % avgPathLength_rand)
    print("Average Path Length of tree with N sorted insertions = %.1f" % avgPathLength_sorted)


if __name__ == '__main__':
    main()