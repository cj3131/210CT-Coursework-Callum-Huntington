"""
Q13: Write the pseudocode for an unweighted graph data structure. You either use an adjacency
matrix or an adjacency list approach. Also, write a function to add a new node and a
function to add an edge. Following that, implement the graph you have designed in the
programming language of your choice. You may use your own linked list from previous labs,
the STL LL, or use a simple fixed size array (10 elements would be fine).

I have used a matrix to represent the edges of the graph. When connecting an edge between
nodes 2 and 4, the 2nd list's 4th element is set to 1. The 4th list's 2nd element is also
set to 1.

Pseudocode:

graph()
    nodes <-- []
    matrix <-- [] * 5
    ADD_NODE(value)
        nodes.append(value)
    ADD_EDGE(a,b)
        matrix[a][b] <-- 1
        matrix[b][a] <-- 1
        
ADD_NODE(value)
    nodesList <-- value

ADD_EDGE(valueA, valueB)
    matrix[valueA][valueB] = 1
    matrix[valueB][valueA] = 1        
"""


class graph():
    def __init__(self):
        self.nodes = [] #A list of nodes
        self.matrix = []
        for i in range(0, 10):
            self.matrix.append([0] * 10) #The matrix is a list of 10 lists, each with 10 elements in them

        print("The empty matrix looks like:  \n")
        for i in range (len(self.matrix)):
            print(self.matrix[i])

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, a, b):
        self.matrix[a][b] = 1 #The b'th element in the a'th list
        self.matrix[b][a] = 1 #Both list a and b need to be updated

    def display(self):
        print("\nThe graph after being filled with nodes and edges:")
        print("\n         0  1  2  3  4  5  6  7  8  9")
        for i in range (0, len(self.matrix)):
            print(i, "     ", self.matrix[i])
    
    def depthFirstSearch(self, node):
        pass

    def breadthFirstSearch(self, node):
        pass

g = graph()
g.addNode(2)
g.addNode(1)
g.addNode(4)
g.addNode(5)
g.addNode(3)
g.addNode(7)
g.addEdge(1,4)
g.addEdge(1,2)
g.addEdge(2,4)
g.addEdge(5,7)
g.addEdge(1,5)
g.addEdge(2,3)
g.display()
