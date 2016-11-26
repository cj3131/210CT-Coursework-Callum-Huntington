"""
Write the pseudocode for an unweighted graph data structure. You either use an adjacency
matrix or an adjacency list approach. Also, write a function to add a new node and a
function to add an edge. Following that, implement the graph you have designed in the
programming language of your choice. You may use your own linked list from previous labs,
the STL LL, or use a simple fixed size array (10 elements would be fine).

Pseudocode:

graph():
    __init__():
        nodes <-- []
        matrix <-- [] * 5
    addNode(value):
        nodes.append(value)
    addEdge(a,b):
        matrix[a][b] <-- 1
        matrix[b][a] <-- 1
    display():
        for i in range (0, length(matrix)):
            print matrix[i]

        
"""

class graph():
    def __init__(self):
        self.nodes = [] 
        self.matrix = []
        for i in range(0, 5):
            self.matrix.append([0] * 5)
        print(self.matrix)

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, a, b):
        self.matrix[a][b] = 1 
        self.matrix[b][a] = 1

    def display(self):
        print("         0  1  2  3  4")
        for i in range (0, len(self.matrix)):
            print(i, "     ", self.matrix[i])
    
    def depthFirstSearch(self, g, node):
        pass

g = graph()
g.addNode(3)
g.addNode(2)
g.addNode(1)
g.addEdge(1,4)
#g.addEdge(2,4)
g.display()
