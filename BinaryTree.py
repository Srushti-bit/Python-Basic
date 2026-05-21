''''
Binary Tree

* Types of Binary tree:

   1) Full inary tree -> Each node has either 0  or 2 children. 
                        NO node has a single child.

   2) Complete Binary Tree -> All levels except possibly the last are completely filled. 
                              Nodes in the last level are filled from left to right.

   3) Perfect Binary tree -> All internal nodes have exactly 2 nodes.
                             All leaf nodes are at the same level.
   4) Balanced Binary Tree

* operations on trees: 

  1) Creation of tree
  2) Insertion of a node
  3) Deletion of a node
  4) search for a value
  5) Traverse all nodes
  6) Deletion of tree   


* Depth First Search types:
    1) pre order - root left right
    2) post order - left right root
    3) inorder - left root right

* Time Complexity: 

INTERVIEW QUES:

q1) why BST?
ans: it performs faster than binary tree when inserting and deleting nodes.

while inserting check 
1st root node is present or not
then check left side is null or node . if it is null then add node 
if not then check
'''

class BSTNode:
    def __init__(self, data):
        self.data = data #50
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    #1st cond to check whether root node has data or is it NULL 
     if rootNode.data is None:  # if Null
         rootNode.data = nodeValue # insert nodevalue i.e 70
         return
     elif nodeValue <= rootNode.data:
         if rootNode.leftChild is None: # check if left node is NULL or not ; if null insert data ;if not then call func i.e recursion
             # node is not present so 1st create obj then assign value
             rootNode.leftChild = BSTNode(nodeValue) #50
             #self.data = data will create new memory to store 50
         else:
             insertNode(rootNode.leftChild, nodeValue)         
     else:
         if rootNode.rightChild is None:
             rootNode.rightChild = BSTNode(nodeValue)        
              #self.data = data will create new memory to store 90
         else:
             insertNode(rootNode.rightChild, nodeValue)  

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=' ')
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)                 
        
def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)
    postorderTraversal(rootNode.rightChild) 
    print(rootNode.data, end=' ')       

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    inOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end = " ")    

def searchNode(rootNode, nodevalue):
    if rootNode.data == nodevalue:
        print("the value is found")
    elif nodevalue < rootNode.data:
                if rootNode.leftChild.data == nodevalue:
                   print("the value is found")
                else:  
                    searchNode(rootNode.leftChild, nodevalue)
    else:
        if rootNode.rightChild.data == nodevalue:
            print("the value is found")  
        else:
            searchNode(rootNode.rightChild, nodevalue)      
         
newBST = BSTNode(None) # obj creation of BSTNode ----after this constructor will be called nad then None is passed and None is saved in data
insertNode(newBST, 70) # root object passing newBST- rootNode; 70- nodeValue
insertNode(newBST, 50) # always check from root object ie from root
insertNode(newBST, 90) 
insertNode(newBST, 30) 
insertNode(newBST, 60) 
insertNode(newBST, 80) 
insertNode(newBST, 100) 
insertNode(newBST, 20)
insertNode(newBST, 40)  

preOrderTraversal(newBST) # pass rootnode address i.e newbst
print()
postorderTraversal(newBST)
print()
inOrderTraversal(newBST)
print()
searchNode(newBST,60)