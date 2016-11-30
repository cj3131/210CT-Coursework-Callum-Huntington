"""
Implement Dijkstra’s algorithm for a weighted graph data structure (you have to update
your previous data structure so that it can deal with weights).
"""
class node():
    def __init__(self, value):
        self.tentativeWeight = float("inf")
        g.addNode(int(value))
        self.value = value
        self.previous = 0

class graph():
    def __init__(self):
        self.nodes = [] 
        self.matrix = []
        for i in range(10):
            self.matrix.append([float("inf")] * 10)
        
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

    def addEdge(self, a, b, weight):
        self.matrix[a.value][b.value] = weight 
        self.matrix[b.value][a.value] = weight

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
                    if value != float("inf"):
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
                    if value != float("inf"):
                        self.searchQueue.append(idx)
        
        print ("visited with breadth first search:  ", self.breadthVisited, "\n\n")
        return self.breadthVisited

    def dijkstra(self, currentNode, destNode, nodeList):
        currentNode.tentativeWeight = 0
        visited = []
        vertexValue = 0
        while currentNode != destNode:
            print("here")
            for idx, value in enumerate(self.matrix[currentNode.value]):
                if value != float("inf"):
                    vertexValue = value
                    if currentNode.tentativeWeight + nodeList[idx].tentativeWeight < nodeList[idx].tentativeWeight:
                        nodeList[idx].tentativeWeight = currentNode.tentativeWeight + nodeList[idx].tentativeWeight
                        nodeList[idx].previous = currentNode
            visited.append(currentNode)
            minimum = float("inf")
            for i in nodeList:
                if i == 0:
                    pass
                
                elif i not in visited and i.tentativeWeight <= minimum:
                    currentNode = i
                    minimum = i.tentativeWeight

        return visited






nodeList = [0]*10
print(nodeList)
g = graph()

nodeOne = node(1)
nodeList[1] = nodeOne
nodeTwo = node(2)
nodeList[2] = nodeTwo
nodeThree = node(3)
nodeList[3] = nodeThree
nodeFour = node(4)
nodeList[4] = nodeFour
nodeFive = node(5)
nodeList[5] = nodeFive
nodeSix = node(6)
nodeList[6] = nodeSix
nodeSeven = node(7)
nodeList[7] = nodeSeven


g.addEdge(nodeOne,nodeFour, 5)
g.addEdge(nodeOne,nodeTwo, 4)
g.addEdge(nodeTwo,nodeFour, 7)
g.addEdge(nodeOne,nodeFive, 2)
g.addEdge(nodeTwo,nodeThree, 1)
g.addEdge(nodeSeven,nodeFour, 3)
g.display()
print("\n\n")
g.depthFirstSearch(1)
g.breadthFirstSearch(1)
print(g.dijkstra(nodeTwo,nodeFive,nodeList))
