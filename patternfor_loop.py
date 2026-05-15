for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()

#==========================================================================================================
# 
n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1):
    for j in range (1,n+1):
        print(chr(64+i), end=" ")
    print()    

#==========================================================================================================

n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1):
    for j in range (1,1+i):
        print("*", end=" ")
    print()

#==========================================================================================================

import time  
n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range (1,i+1):
        time.sleep(3)
        print("*", end=" ")
    print()    

#==========================================================================================================
# prduct of Array Except self
 #Ques) given an array, return an array where each element is the product of all the elements in the array except itself
 #sample: [1,2,3,4]
 #output: [24,12,8,6]
