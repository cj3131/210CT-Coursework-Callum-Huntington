"""
Based on the Python code or the C++ code provided in class as a starting point,
implement the double linked list node delete function.
"""
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

    # starting from the beginning of the list, iterate through until we get to the node to be deleted
    def delete(self,nodeValue):
        current = self.head

        while current != None:
            if current.value == nodeValue:
                # when it is found, if it is not the first item in the list, set the previous node's
                # "next" attribute to the current node's next attribute, and the next node's "prev"
                # attribute to the current node's previous node.
                if current.prev != None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    # this happens if the node being deleted is the first node.
                    self.head = current.next
                    current.next.prev = None
            current = current.next



          
if __name__ == '__main__':
    l=List()

    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(7))
    l.insert(l.head,Node(8))
    l.insert(l.head,Node(10))
    l.insert(l.head,Node(13))
    l.insert(l.head,Node(15))
    l.display()
    l.delete(7)
    l.display()
    l.delete(10)
    l.display()