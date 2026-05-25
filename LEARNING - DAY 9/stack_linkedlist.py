'''
Stack Using Linked List:

Instead of using an array, we use a linked list, where each node contains:
    1) data
    2) next pointer
The top of the stack is the head of the linked list.


* Basic Operations
    1. Push (Insert at beginning)
        Create a new node
        Point its next to current top
        Move top to new node

    2. Pop (Remove from beginning)
        Store top node
        Move top to next node
        Delete old top
        
    3. Peek
        Return data of top node
'''

class Node:
    def __init__(self, value = None):
        self.value =  value # creates separate memory for each new value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next   

# implementing linkedlist through stack 
# make stack class

class Stack:    
    # in stack constructor linkedlist obj creates
    def __init__(self):
        self.Linkedlist = Linkedlist()

    def __str__(self):    # __str__ in Python is a special method used to define how an object is converted into a string.
        values= [str(x.value) for x in self.Linkedlist]
        return '\n'.join(values)    
    
    def isEMPTY(self):
        if self.Linkedlist.head == None:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEMPTY():
            return "There is no element in the stack"
        else:
            nodeValue = self.Linkedlist.head.value # accesses the data/value stored inside that node.; stores that value in a variable named nodeValue.
            self.Linkedlist.head = self.Linkedlist.head.next
            return nodeValue
        
    def push(self, value):
        node = Node(value)
        node.next = self.Linkedlist.head # new node's next is assigned to head's next
        self.Linkedlist.head = node # then new node is head

    def peek(self):
        if self.isEMPTY():
            return "there is not any element in the stack"
        else:
            nodeValue = self.Linkedlist.value
            return nodeValue

    

# CREATE STACK OBJECT 
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("Display Top value: ")
print(customStack.peek())
print("pop top element")
print(customStack.pop())
print("now check the stack again")
print(customStack)
print("pop top element")
print(customStack.pop())
print("now check the stack again")
print(customStack)






















