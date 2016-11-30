"""
Implement Dijkstra’s algorithm for a weighted graph data structure (you have to update
your previous data structure so that it can deal with weights).
"""
class node():
    def __init__(self, value):
        self.tentativeWeight = float("inf")
        g.addNode(value)

class graph():
    def __init__(self):
        self.nodes = [] 
        self.matrix = []
        for i in range(10):
            self.matrix.append([0] * 10)
        
        print("The basic matrix looks like:  \n")
        for i in range (len(self.matrix)):
            print(self.matrix[i])

        #related to searching
        self.depthVisited = []
        self.breadthVisited = []
        self.searchStack = []
        self.searchQueue = []

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, a, b):
        self.matrix[a][b] = 1 
        self.matrix[b][a] = 1

    def display(self):
        print("\n\nHere is the matrix with all of the edges added.\n")
        print("         0  1  2  3  4  5  6  7  8  9")
        for i in range (0, len(self.matrix)):
            print(i, "     ", self.matrix[i])
    
    def depthFirstSearch(self, node):
        self.searchStack.append(node) # add the current node onto the stack
        while self.searchStack: # when the stack is empty, all nodes have been visited
            node = self.searchStack.pop() # pop the node currently being viewed into node
            if node not in self.depthVisited: # if the node currently being viewed is not in the visited list
                self.depthVisited.append(node) # add it to the visited list
                print("visited via depth first search so far:  ", self.depthVisited, "\n")
                
                for idx, value in enumerate(self.matrix[node]):
                    if value == 1:
                        self.searchStack.append(idx)

        print("visited with depth first search:  ", self.depthVisited, "\n\n")
        return self.depthVisited

    def breadthFirstSearch(self, node):
        self.searchQueue.append(node)
        while self.searchQueue:
            node = self.searchQueue.pop(0)
            if node not in self.breadthVisited:
                self.breadthVisited.append(node)
                print("visited via breadth first search so far:  ", self.breadthVisited, "\n")

                for idx, value in enumerate(self.matrix[node]):
                    if value == 1:
                        self.searchQueue.append(idx)
        
        print ("visited with breadth first search:  ", self.breadthVisited)
        return self.breadthVisited

    def dijkstra(self, currentNode, destNode):
        currentNode.tentativeWeight = 0
        visited = []
        while currentNode != destNode:
            for idx, value in enumerate(self.matrix[node]):
                if value == 1:
                    if currentNode.tentativeWeight + """v[u].tentativeWeight""" < """u.tentativeWeight""":
                        u.tentativeWeight = currentNode.tentativeWeight + currentNode"""[u]""".tentativeWeight
                        """u.previous""" = currentNode
            visited.append(currentNode)
            minimum = float("inf")
            """for i in currentNode:"""
                """if i not in visited and i.tentativeWeight < minimum:"""
                    currentNode = i
                    minimum = i.tentativeWeight

        return currentNode.tentativeWeight





g = graph()
nodeThree = node(3)
nodeTwo = node(2)
nodeOne = node(1)
nodeFive = node(5)
nodeFour = node(4)
g.addEdge(1,4)
g.addEdge(1,2)
g.addEdge(2,4)
g.addEdge(1,5)
g.addEdge(2,3)
g.display()
print("\n\n")
g.depthFirstSearch(1)
g.breadthFirstSearch(1)
g.dijkstra(2,5)