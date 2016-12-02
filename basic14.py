"""
Q14: Implement BFS and DFS traversals for the above graph. Save the nodes traversed in
sequence to a text file.

In this implementation BFS uses a queue, DFS uses a stack. Apart from the data structure they use both
work in similar ways, BFS checks and prints all nearby nodes before moving on, while DFS moves as far through
the list as possible before carrying on. This happens because after node X’s connecting nodes have been added to
the searchStack or searchQueue, BFS pops from the front, meaning all of X’s connected nodes will be printed
before further nodes are dealt with. DFS and it’s stack on the other hand will always deal with the most recently
discovered node.
"""

class graph():
    def __init__(self):
        self.nodes = [] #A list of nodes
        self.matrix = []
        for i in range(10):
            self.matrix.append([0] * 10)  #The matrix is a list of 10 lists, each with 10 elements in them

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
        self.matrix[a][b] = 1 #The b'th element in the a'th list
        self.matrix[b][a] = 1 #Both list a and b need to be updated

    def display(self):
        print("\n\nHere is the matrix with all of the edges added.\n")
        print("         0  1  2  3  4  5  6  7  8  9")
        for i in range (0, len(self.matrix)):
            print(i, "     ", self.matrix[i])
    
    def depthFirstSearch(self, node):
        self.searchStack.append(node) # add the node we are beginning with onto the stack
        while self.searchStack: # when the stack is empty, all nodes have been visited
            node = self.searchStack.pop() # pop the most recently added node 
            if node not in self.depthVisited: # if the node currently being viewed has not been visited
                with open("depthVisited.txt", "a") as file:
                    file.write(str(node))
                self.depthVisited.append(node) # write it into the file and add it to the visited list
                print("visited via depth first search so far:  ", self.depthVisited, "\n")
                
                for idx, value in enumerate(self.matrix[node]):
                    #Check every value in the current list, if there is an edge with another node, add it to the stack
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
                with open("breadthVisited.txt", "a") as file:
                    file.write(str(node))
                print("visited via breadth first search so far:  ", self.breadthVisited, "\n")

                for idx, value in enumerate(self.matrix[node]):
                    if value == 1:
                        self.searchQueue.append(idx)
        
        print ("visited with breadth first search:  ", self.breadthVisited)
        return self.breadthVisited




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
print("\n\n")
with open ("depthVisited.txt", "w") as file:
    pass
g.depthFirstSearch(1)
with open("breadthVisited.txt", "w") as file:
    pass
g.breadthFirstSearch(1)
