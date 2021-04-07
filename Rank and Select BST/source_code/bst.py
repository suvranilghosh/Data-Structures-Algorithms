'''
Finding rank of an element:rank() and 
selection of an element with a specified rank: select() in a BST
execution instructions: 
under ./Q3/source_code/ directory
> python bst.py <file_name>
example:
python bst.py HW2.txt
'''
import time
import random
import sys
from sys import argv

# change accordingly
RANK_INPUT = 7
SELECTION_INPUT = 7
sorted = []

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.leftSize = 0

    def insertNode(self, node):
        # values greater than parent goes right and less ones go left
        # done recursively if the immediate child is not empty
        if node.key > self.key: 
            if self.right is None:
                self.right = node
            else:
                self.right.insertNode(node)
        else:
            self.leftSize += 1
            if self.left is None:
                self.left = node
            else:
                self.left.insertNode(node)

    def rank(self, key):

        if key == self.key:
            return self.leftSize
        if key < self.key:
            if self.left is None:
                return -1
            else:
                return self.left.rank(key)
        else:
            if self.right is None:
                return -1
            else:
                rightSize = self.right.rank(key)
                if rightSize == -1:
                    # x not found in right sub tree, i.e. not found in tree
                    return -1
                else:
                    return 1 + self.leftSize + rightSize

    def select(self, k):
        t = self.leftSize
        # print(t)
        found = -1
        if t>k:
            if self.left is not None:
                self.left.select(k)
            # else:
            #     return -1
        elif t<k:
            if self.right is not None:
                self.right.select(k-t-1)
            # else:
            #     return -1
        else:
            print("Select(%d) is ="%SELECTION_INPUT, self.key)
            return self.key
        return self.key

 
class Tree:
    def __init__(self):
        self.root = None
 
    def add(self, key):
        new_node = Node(key)
        # if root of tree/subtree is empty add node to root
        # else use insertNode function
        if self.root is None:
            self.root = new_node
        else:
            self.root.insertNode(new_node)

    def rank(self, key):
        # if tree is empty then return -1 or else call root.rank(key)
        if self.root is None:
            return -1
        else:
            return self.root.rank(key)

    def select(self, rank):
        # if tree is empty then return -1 or else call root.select(rank)
        if self.root is None:
            return -1
        return self.root.select(rank)

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
    
    sys.setrecursionlimit(2000)
    bst = Tree()
    
    for num in data:
        bst.add(num)
    
    print("Rank(%d) is ="%RANK_INPUT, bst.rank(RANK_INPUT))
    print("Select(%d) is ="%SELECTION_INPUT, bst.select(SELECTION_INPUT))
    # bst.select(SELECTION_INPUT)
    
if __name__ == '__main__':
    main()

