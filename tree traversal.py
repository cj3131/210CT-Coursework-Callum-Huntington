"""
Implement TREE_SORT algorithm in a language of your choice, but make sure that the
INORDER function is implemented iteratively.
"""

class Node:
     
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
def inOrder(root):
    current = root 
    s = []
    done = 0
     
    while True:
        if current != None:
            s.append(current)
            current = current.left 
        else:
            if (s != [] ):
                current = s.pop()
                print(current.data)
                current = current.right 
            else:
                break
 
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)