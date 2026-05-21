class Node:
    def __init__(self, value = None):
        self.value =  value # creates separate memory for each new value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next          

class Queue:
    def __init__(self):
        self.linkedlist = Linkedlist()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enQueue(self, value):
        newNode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def isEMPTY(self):
        if self.Linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEMPTY():
            return "there is no any node in queue"
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode               

    def peek(self):
        if self.isEMPTY():
            return "there is not any element in the queue"
        else:
            nodeValue = self.Linkedlist.value
            return nodeValue
        
    def delete(self):
        self.linkedlist.head = None   
        self.linkedlist.tail = None  

customqueue = Queue()
customqueue.enQueue(1)
customqueue.enQueue(2)
customqueue.enQueue(3)  
print(customqueue)
print("display top value")  
print(customqueue.peek())
print("delete fifo")
print(customqueue.dequeue())
print("display queue again")
print(customqueue)
print("delete fifo")
print(customqueue.dequeue())
print("display queue again")
print(customqueue)