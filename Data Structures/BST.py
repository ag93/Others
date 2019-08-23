# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None        
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self.add(val, self.root)
            
    def add(self, val, root):
        if (val < root.value):
            if(root.left is not None):
                self.add(val, root.left)
            else:
                root.left = Node(val)
        else:
            if(root.right is not None):
                self.add(val, root.right)
            else:
                root.right = Node(val)
                
    def printTree(self):
        if(self.root is not None):
            self.print_(self.root)
            
    def print_(self, node):
        if(node is not None):
            self.print_(node.left)
            print(str(node.value) + " ")
            self.print_(node.right)

    def getRoot(self):
        return self.root

    def find(self, val):
        if(self.root is not None):
            return self._find(val, self.root)
        else:
            return( "Not Found!")

    def _find(self, val, node):
        
        if(val < node.value and node.left is not None):
            return self._find(val, node.left)
            
        elif(val > node.value and node.right is not None):
            return self._find(val, node.right)
                       
        elif(node.value == val):
            return( "Node of value " + str(val) + " found!!")
            
        else:
            return("Node of value " + str(val) + " Not Found")
        

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

tree = Tree()
tree.add_node(10)
tree.add_node(5)
tree.add_node(20)
tree.add_node(3)
tree.add_node(7)
tree.add_node(15)

tree.printTree()

print(tree.find(10))
print(tree.find(5))
print(tree.find(20))
print(tree.find(3))
print(tree.find(7))
print(tree.find(15))
print(tree.find(21))

tree.deleteTree()
tree.printTree()  

    