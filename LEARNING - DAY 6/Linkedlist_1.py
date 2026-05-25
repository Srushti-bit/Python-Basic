class Node:
    def __init__(self,data):    # self,data--constructor
        self.data = data  # instance variable(5)(10)
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None 
        self.tail = None


    def addNode(self, value):
        self.node = Node(value)  #obj creation
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node
            self.tail = self.node

    def addNodeBeginning(self, value):
        print("Add node in begining")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node

    def addNodeBetween(self, index, value):  #index → position where node should be inserted;value → data to store in new node
        new_node = Node(value)   #Creates a new node with given value
        if self.head is None:  # Checks if linked list is empty
            self.head = new_node
                                     #Makes new node the first and last node
            self.tail = new_node
        elif index == 0:      # Checks if insertion is at beginning
            new_node.next = self.head   # Connects new node to current first node
            self.head = new_node     # Makes new node the new first node
        else:                     # Runs when insertion is NOT at beginning ; Used for middle/end insertion
            temp = self.head      # Starts traversal from first node
            for _ in range(index -1):  # Moves temp to the node before insertion position
                temp = temp.next  # Moves temp one step forward
                new_node.next = temp.next # New node points to next node
                temp.next = new_node    # Previous node (20) points to new node (25)


               
    def display(self):
        while self.head is not None:
            print(self.head.data,'|',self.head.next,'->',end=' ')
            self.head = self.head.next
        print()

if __name__ == '__main__':
    object = Linkedlist()
    while True:
        print("1. add node Linkedlist: ")   
        print("2. add node in begning: ")       
        print("3. add node in between: ")  
        print("4. add node in end: ")  
        print("5. display Linked list: ")  
        print("6. Exit")  

        ch = int(input('Enter your choice: '))

        if ch == 1:
            value = int(input('Enter the value for node: '))
            object.addNode(value)
            print("Node added successfully in single Linkedlist:")

        elif ch == 2:
            value = int(input('Enter the value for node: '))
            object.addNodeBeginning(value)  

        elif ch == 3:
                 index = int(input("Enter index position: "))
                 value = int(input("Enter value for node: "))

                 object.addNodeBetween(index, value)

                 print("Node inserted successfully")
  
        elif ch == 5:
            object.display()

        elif ch == 6:
            break

        else:
            print("invalid")    
        