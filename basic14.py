"""
Implement BFS and DFS traversals for the above graph. Save the nodes traversed in
sequence to a text file.
"""

class graph():
    def __init__(self):
        self.nodes = [] 
        self.matrix = []
        for i in range(0, 9):
            self.matrix.append([0] * 10)
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
        searchStack = [] # each new node we go to will be added to the stack
        visited = [] # will contain a list of all the nodes that have been visited
        temp = 0 # will contain the node currently being viewed

        searchStack.push(node) # add the current node onto the stack
        while searchStack != []: # when the stack is empty, all nodes have been visited
            temp = searchStack.pop() # pop the node currently being viewed into temp
            if temp not in visited: # if the node currently being viewed is not in the visited list
                visited.append(temp) # add it to the visited list
                searchStack.extend(graph[node] - visited)
                
                #for all edges, e, from temp, S.push(e.to)
        return visited 

g = graph()
g.addNode(3)
g.addNode(2)
g.addNode(1)
g.addEdge(1,4)
#g.addEdge(2,4)
g.display()
print("\n\n\n")
g.depthFirstSearch()
