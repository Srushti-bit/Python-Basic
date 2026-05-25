# Ques 1)
# input = [79, 77, 54, 81, 48, 34, 25, 16]
# output = 3 
# the areas that arre in square form are 81, 25 and 16   -----WIPRO QUES---

import math
input = [79, 77, 54, 81, 48, 34, 25, 16]
count=0
for i in range (len(input)):
    root = int(math.sqrt(input[i]))
    if root * root == input[i]:
        count +=1
print(count)    # ans: 3

# Ques 2)

fruit = {}          #{'Apple' : 1, 'Banana' : 1, 'apple' : 1}
def addone(index):
    if index in fruit:
        fruit[index] +=1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))    # ans: 3
print(fruit)         # {'Apple': 1, 'Banana': 1, 'apple': 1}

# Ques 3)

# Wap to accept student name and marks from the keyboard and creates a dictionary. 
# also display student marks by taking student name.

n = int(input("Enter the number of students: ")) #2
d ={}
for i in range(n):
    name = input("Enter the student Name: ")
    marks = input("Enter student Marks: ")
    d[name] = marks  #add key:value
while True:
    name= input("Enter student name to get marks: ")
    marks=d.get(name, -1)    # if name does not exists then it returns -1
    if marks == -1:
        print("Student Not Found")
    else:
        print("the marks of ",name,"are",marks)
    option = input("Do you want to find another student marks[yes|No]")
    if option == "No":
        break
    print("Thanks for using our application")        

# Ques 4)

# WAP to access each character of string in forward and backward direction by using while loop ?
# i/p = "Learning python is very easy."

input = "Learning Python is very easy"
n=len(input)
i = 0
print("Forward Direction: ")
while i < n:
    print(input[i], end = '')
    i += 1

print("\nBackward Direction: ")
i = -1
while i >= -n:
        print(input[i], end = '')
        i -= 1
#============================================================================

# Ques 5)

# input = "abcdfjgerj  abcdfjger"
# output = j

str = "abcdfjgerj abcdfjger"
a, b = str.split()
print(str)
for ch in str:
    if a.count(ch)!=b.count(ch):
        print(ch)
        break    # ans: j

#=====================================================
# List Comprehension
# Ques 6)
# v=['a','e','i','o','u']
     
v=['a','e','i','o','u']
w = input("Enter the word where we still search the vowels: ")
found= []
for i in w:
    if i in v:
        if i not in found:
            found.append(i)
print('Found vowels = ',found)
print('Unique vowels',len(found),'from the given word= ',w)            

#==================================================================================
    
# Ques 7)

# input= 6,30,50
# 29,38,12, 48, 39, 55
#output = 38, 48, 39

x, y, z = map(int, input().split())

mylist = []

for i in range(x):
    a = int(input())
    mylist.append(a)

for j in mylist:
    if y <= j <= z:
        print(j, end=" ")

#======================================================
# # Ques 8)

import datetime

date=datetime.datetime.now()
print("it's mow:{:%d/%m/%Y %H/%H/%S}".format(date))

#=================================================

# Ques 9)

x=['A', 'B', 'C']
y=['A', 'B', 'C']
z= [1,2,3,4]
print(x==y)
print(x==z)
print(x!=z)

# ans: True    ---checking addressess not values
# False
# True

#===============================================

# Ques 10)

# s = [1,4,9,16,25,36,49,64,81,100]  --given for confusion (not needed)
val=[2**i for i in range(1,6)]  #i =1,2,3,4
print(val)  # ans: [2, 4, 8, 16, 32]

#==============================================================

#  Ques 11)

s = [i*1 for i in range(1,11)]
print(s)  # ans: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#==============================================================
#   --dictionary comparision
#Ques 12)
squares={x:x*x for x in range(1,6)}  #i =1,2,3,4
print(squares)
# ans: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Ques 12.1)

doubles = {x:2*x for x in range(1,6)}
print(doubles)  # ans: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

#Ques 12.2)

a,b=[int(x) for x in input("Enter 2 numbers: ").split()]
print("product is: ", a*b)
# ans: Enter 2 numbers: 3 4
# product is:  12

#Ques 12.3)

a,b,c=[float(x) for x in input("Enter 3 float numbers: ").split(',')]
print("the sum is : ",a+b+c)
# ans: Enter 3 float numbers: 2,3,4
# the sum is :  9.0

#==============================================================================

# FOR LOOP WITH ELSE

# ques 13)
 
mycart=[10,20,800,60,70]
for item in mycart:
    if item>400:
        print("this is not in my budget")
        continue
    print(item)
else:
    print("you have purchased everything")    

#==============================================================================
# Ques 14)

#username = "admin"
#password = "admin"

#Enter username
#Enter password

right_username = "admin"
right_password = "admin"

username =""
password = ""
while username != right_username and password != right_password:
        username = input("enter username: ")
        password = input("enter password: ")
        
print("login successfully")    

