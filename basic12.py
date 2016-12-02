"""
Q12: Implement TREE_SORT algorithm in a language of your choice, but make sure that the INORDER
function is implemented iteratively.

Every node has a left and right attribute, and the inorder function moves through the nodes
by going to the leftmost node, printing it, then moving back up the stack to check the right
node, and checking the left most node from there again. A stack is used to keep track
of which node we are dealing with, and which node needs to be checked next.
"""

class Node:     
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None
 
def inOrder(rootNode):
    current = rootNode 
    stack = []
    print("Result of the inOrder function:")

    while True:
        if current != None: # current will equal none if the current node has no left node
            stack.append(current)
            current = current.left 
        else:
            if (stack != [] ): # if the stack is empty, we have reached the rightmost node.
                current = stack.pop() 
                print(current.value)
                current = current.right # if a node has no right node, we will be checking it's parent in the next iteration
            else:
                break
 
while True:
    try:
        rootNode = Node(int(input("Enter the value of the tree's root node.  ")))
        rootNode.left = Node(int(input("Enter the value of the root node's left child node.  ")))
        rootNode.right = Node(int(input("Enter the value of the root node's right child node.  ")))
        rootNode.left.left = Node(int(input("Enter the value of the root node's left child's left child.  ")))
        rootNode.left.right = Node(int(input("Enter the value of the root node's left child's right child.  ")))
        rootNode.right.left = Node(int(input("Enter the value of the root node's right child's left child.  ")))
        rootNode.right.right = Node(int(input("Enter the value of the root node's right child's right child.  ")))
        break
    except:
        print("Only enter integers for node values.")

inOrder(rootNode)
