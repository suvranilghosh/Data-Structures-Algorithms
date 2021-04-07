'''
next(): returns the next smallest number in the BST
hasNext(): returns True if the tree is not empty and False otherwise
Only Node and BSTIterator classes along side functions definitions 
are given as per the question in the assignment

******************************
Please use your own drive code
******************************
'''
# Node class
class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    
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

# Tree class with next() and hasNext()
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.node = root
        self.list = []
    
    def add(self, key):
        new_node = TreeNode(key)
        # if root of tree/subtree is empty add node to root
        # else use insertNode function
        if self.root is None:
            self.root = new_node
        else:
            self.root.insertNode(new_node)

    def next(self):
        # traverse to the leftmost leaf while pushing each
        # key along the way into the list 
        while self.node:
            self.list.append(self.node)
            self.node = self.node.left

        # return the last element of the list
        self.node = self.list.pop()
        next_smallest = self.node.key

        # check right child
        self.node = self.node.right
        return next_smallest

    def hasNext(self):
        # return True iff list is not empty or current node != None
        return self.list or self.node
