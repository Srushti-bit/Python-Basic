# stack implementation without size limit

# import sys
# class Stack:
#     def __init__(self):
#      self.myStack = []  #Creating stack
 
#     def push(self, value):
#           self.myStack.append(value)
#           print("Element push")

#     def display(self):
#           print(self.myStack)    

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):     # removes permanentely from the memory
#         if self.isEmpty():
#             print("Stack is Empty")    
#         else:
#             print(self.myStack.pop())         

#     def peek(self):  #returns last operator first
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack[-1])            # or print(len(myStack[-1]))

#     def delete(self):
#         self.myStack = None        

# obj = Stack()
# print("Stack has created: ")
# while True:
#     print("1. push operation: ")
#     print("2. Display Stack: ")
#     print("3. pop operation")
#     print("4. peek operation")
#     print("5. Delete stack")
#     print("7. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#          value = int(input("Enter value to push in stack: "))
#          obj.push(value)
#     elif choice == 2:
#          obj.display()
#     elif choice == 3:
#         obj.pop()    
#     elif choice == 4:
#         obj.peek()  
#     elif choice == 5:
#         obj.delete()      
#     else:
#         sys.exit()          
         
#======================================================================================================
#      
# stack implementation with size limit

import sys
class Stack:
    def __init__(self,size):
     self.myStack = []
      #Creating stack
     self.stackSize = size   # stack size defined
 
    def push(self, value):
          if self.isFull():
              print("Stack is full")
          else:
              self.myStack.append(value)
              print("element push")

    def display(self):
          print(self.myStack)    

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
        
    def isFull(self):
        if self.isFull():
           return len(self.myStack) == self.stackSize     
        
    def pop(self):     # removes permanentely from the memory
        if self.isEmpty():
           return len(self.myStack) == self.stackSize   
        else:
            print(self.myStack.pop())         

    def peek(self):  #returns last operator first
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack[-1])           # or print(len(myStack[-1]))

    def delete(self, size):
        self.myStack = None  

size = int(input("Enter the size of Stack: "))
obj = Stack(size)
print("Stack has created: ")
while True:
    print("1. push operation: ")
    print("2. Display Stack: ")
    print("3. pop operation")
    print("4. peek operation")
    print("5. Delete stack")
    print("6. check empty")
    print("7.check full")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
         value = int(input("Enter value to push in stack: "))
         obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()    
    elif choice == 4:
        obj.peek()  
    elif choice == 5:
        obj.delete()  
    elif choice == 6:
        obj.isEmpty()    
    elif choice == 7:
        obj.isFull()        
    else:
        sys.exit()      

#=================================================================================

