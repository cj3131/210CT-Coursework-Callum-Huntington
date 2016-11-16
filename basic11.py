class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))
    def delete(self,n):
      n.prev.next = n.next
      n.next.prev = n.prev
      n.next = None
      n.prev = None


        
if __name__ == '__main__':
    l=List()

    elementone = Node(4)
    elementtwo = Node(6)
    elementthree = Node(8)
    l.insert(None, elementone)
    l.insert(l.head, elementtwo)
    l.insert(l.head, elementthree)
    #print(l.head)
    #l.insert(l.head, Node(13))
    l.delete(elementtwo)
    l.display()