'''
Trees - Non linear DS
- File system in a computer
- in blockchain

- quicker and easier access to data

Tree Terminology in Data Structure 🌳
1. Node

Each element in a tree is called a node.

2. Root Node

Topmost node of the tree.

3. Parent Node

A node that has child nodes.

4. Child Node

Node connected below another node.

5. Sibling Nodes

Nodes having same parent.

6. Leaf Node

Node having no children.

7. Edge

Connection between two nodes.

8. Path

Sequence of connected nodes.

10. Depth of Node

Distance from root node to a particular node.

11. Subtree

Smaller tree inside main tree.

12. Degree of Node

Number of children a node has.

13.Ancestor in Tree 

An ancestor is any node that comes above a node in the path from root.

* Python List in Tree Data Structure:-

In Tree DS, Python lists are used to:

store tree nodes
represent children
implement trees easily
'''

class Tree:
    def __init__(self,data):
        self.data = data #("Drinks") ("Hot") ("Cold") ("Tea") ....--every time separate memory is creating
        self.child = []  #list representation

    def __str__(self, level = 0): 
        ret = " "* level + str(self.data) + "\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret

    def addChild(self, object): # creating method: self as a construtor & object- parameter   
        self.child.append(object)
        print("Tree node added") 
        
rootNode = Tree("Drinks")        
Hot = Tree("Hot")
Cold = Tree("Cold")
Tea = Tree("Tea")
Coffee = Tree("Coffee")
NonAlcholic = Tree("NonAlchoholic")
Alcholic = Tree("Alcholic")

rootNode.addChild(Hot)  #left Child
rootNode.addChild(Cold)  # right child
Hot.addChild(Tea)  #left Child
Hot.addChild(Coffee) # right child
Cold.addChild(NonAlcholic) #left Child
Cold.addChild(Alcholic)  # right child

print(rootNode) # as soon as this rootNode executes strng method

#==========================================================================

class Tree:
    def __init__(self,data):
        self.data = data #("Drinks") ("Hot") ("Cold") ("Tea") ....--every time separate memory is creating
        self.child = []  #list representation

    def __str__(self, level = 0): 
        ret = " "* level + str(self.data) + "\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret

    def addChild(self, object): # creating method: self as a construtor & object- parameter   
        self.child.append(object)
        print("Tree node added") 
        
rootNode = Tree("N1")        
N2 = Tree("N2")
N3 = Tree("N3")
N4 = Tree("N4")
N5 = Tree("N5")
N6 = Tree("N6")
N7 = Tree("N7")
N8 = Tree("N8")

rootNode.addChild(N2)  #left Child
rootNode.addChild(N3)  # right child
N2.addChild(N4)  #left Child
N2.addChild(N5) # right child
N3.addChild(N6) #left Child
N3.addChild(N7)
N3.addChild(N8)
print(rootNode) # as soon as this rootNode executes strng method




