# QUEUE ---FIFO

import sys
class Queue:
    def __init__(self, size):  #Parametrized constructor (for one obj one constructor will call)
        self.myQueue = []    
        self.queueSize = size

    def isFull(self):
        if len(self.myQueue) == self.queueSize:
             return True
        else:
             return False   

    def enQueue(self, value):
        if self.isFull():
              print("Queue is full")
        else:
              self.myQueue.append(value)
                  
    def display(self):
        print(self.myQueue) 

    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False       

    def deQueue(self):
         if self.isEmpty():
              print("Queue is Empty")
         else:
              self.myQueue.pop(0)    
        
    def peek(self):
         if self.isEmpty():
              print("Queue is empty") 
         else:
              print(self.myQueue[0])

    def deleteQueue(self):
         self.myQueue = None                  

size = int(input("Enter the size of Queue: "))
obj = Queue(size)   # this is obj also called as call by reference
print("Queue has created")   
while True:
    print("1. Enqueue operation: ")  # add a element in a Queue
    print("2. Display Queue: ")
    print("3. DeQueue operation: ")
    print("4. peek operation: ")
    print("5. Delete Queue: ")
    print("6. Exit ")
    choice = int(input("Enter your choice: "))
  
    if choice == 1:
        value = int(input("Enter element to add in Queue: "))
        obj.enQueue(value)

    elif choice == 2:
         obj.display()

    elif choice == 3:
         obj.deQueue()   

    elif choice == 4:
         obj.peek()  

    elif choice == 5:
         obj.deleteQueue()   

    elif choice ==6:
         sys.exit(0)

    else:
         print("Invalid")     
       
# TIME COMPLEXITY OF Queue

'''                tc             sc
1. create Queue   O(1)             O(1)
2.Enqueue         O(n)              O(1)
3.Dequeue                           O(1)
4.peek                              O(1)
5.isEmpty                           O(1)
6.Delete entire Queue                O(1)
'''


         
                 


