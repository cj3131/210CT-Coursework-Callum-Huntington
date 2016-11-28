"""
Implement TREE_SORT algorithm in a language of your choice, but make sure that the INORDER
function is implemented iteratively.
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
    print("Result of the inOrder function:")
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
 

root = Node(int(input("Enter the value of the tree's root node.  ")))
root.left = Node(int(input("Enter the value of the root node's left child node.  ")))
root.right = Node(int(input("Enter the value of the root node's right child node.  ")))
root.left.left = Node(int(input("Enter the value of the root node's left child's left child.  ")))
root.left.right = Node(int(input("Enter the value of the root node's left child's right child.  ")))
root.right.left = Node(int(input("Enter the value of the root node's right child's left child.  ")))
root.right.right = Node(int(input("Enter the value of the root node's right child's right child.  ")))
inOrder(root)