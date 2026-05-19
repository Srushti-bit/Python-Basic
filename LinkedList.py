class Node:
    def __init__(self,data):
        self.data = data  # instance variable
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

linkedlist = Linkedlist()
linkedlist.head = Node(5)
second =   Node(10)  # creating new objs means creating new nodes --as each obj has separate memory
third = Node(15)
fourth = Node(20)

#connecting nodes
linkedlist.head.next = second
second.next = third
third.next = fourth

#display linkedlist

while linkedlist.head.next != None:
    print(linkedlist.head.data,"|", linkedlist.head.next,"->",end = " ")
    linkedlist.head = linkedlist.head.next

if __init__ == '__main__':
    object = Linkedlist()
    while True
