class graph():
    def __init__(self):
        self.nodes = [] 
        self.matrix = [ [0] * 5 ] * 5
        #print(self.matrix)

    def addNode(self, value):
        self.nodes.append(value)
        #self.matrix[value] = []
        
        #print(self.matrix)

    def addEdge(self, a, b):
        self.matrix[a][b] = 1 #.append(b)
        #print("This is a ", self.matrix[a])
        #print("This is b ", self.matrix[b])

        self.matrix[b][a] = 1 #.append(a)

    def display(self):
        #print( self.matrix )
        print("         0  1  2  3  4  5")
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

