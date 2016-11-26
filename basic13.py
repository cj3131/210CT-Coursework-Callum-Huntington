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
    
    def DFS(self):
        pass

g = graph()
g.addNode(3)
g.addNode(2)
g.addNode(1)
g.addEdge(1,4)
#g.addEdge(2,4)
g.display()
