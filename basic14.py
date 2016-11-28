"""
Implement BFS and DFS traversals for the above graph. Save the nodes traversed in
sequence to a text file.
"""

class graph():
    def __init__(self):
        self.nodes = [] 
        self.matrix = []
        for i in range(10):
            self.matrix.append([0] * 10)
        print(self.matrix, "\n\n\n")

        #related to DFS
        self.visited = []
        self.searchStack = []

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, a, b):
        self.matrix[a][b] = 1 
        self.matrix[b][a] = 1

    def display(self):
        print("         0  1  2  3  4  5  6  7  8  9")
        for i in range (0, len(self.matrix)):
            print(i, "     ", self.matrix[i])
    
    def depthFirstSearch(self, g, node):
        temp = 0 # will contain the node currently being viewed
        counter = 0

        self.searchStack.append(node) # add the current node onto the stack
        while self.searchStack != []: # when the stack is empty, all nodes have been visited
            temp = self.searchStack.pop() # pop the node currently being viewed into temp
            if temp not in self.visited: # if the node currently being viewed is not in the visited list
                self.visited.append(temp) # add it to the visited list
                for i in self.matrix[node]:
                    counter += 1 
                    if i == 1:
                        if counter in self.visited:
                            pass
                        else:
                            #GO BACK TO SEARCHSTACK.PUSH
                            g.depthFirstSearch(g, counter)

        return self.visited

g = graph()
g.addNode(3)
g.addNode(2)
g.addNode(1)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(2,3)
g.display()
print("\n\n\n")
print(g.depthFirstSearch(g, 1))