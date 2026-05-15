'''A list in Python is a collection used to store multiple items in a single variable.

It is:

Ordered
Mutable
Allows duplicate values
Supports different data types'''

mylist = ["prashant", "Ashish", "Komal", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]

print(mylist)
print(type(mylist))
print(mylist[0]) #prashant
print(mylist[1])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5]) #n=5 n-1=4
print(mylist[1:]) #n-1 8-1=7
print(mylist[1:8:2]) # 1 3 5 7

#=================================================================================

mylist[2] = "Akshay"
print(mylist)

#=================================================================================

if "ankush" in mylist:
    print("yes")
else:
    print("not present")    

#=================================================================================
mylist.append('harsh')
mylist.append("laxman")
print(mylist)           #---- append() and extend() both work like same 

#=================================================================================
# to add an item at specific position

mylist.insert(3,"sanket")
print(mylist)

#=================================================================================
# remove method

mylist.remove("sandip")
print(mylist)

#=================================================================================
# cloning

newlist = mylist.copy()
print(newlist)

#=================================================================================
# NESTED LIST

mylist = [['prashant', 'jha'],['85,56'],[440022, "yyy"]]
print("example of multidimensional list: ")
print(mylist)

print(mylist[row][col])

print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

#LOGIC 
#[    0                 1
# 0=['prashant',     'jha'], 
# 1=['85,              56'],
# 2=[440022,           "yyy"]]

#=================================================================================

list2=[50,25.50,'prashant']
del list2[2]
#del list2
print(list2)

#=================================================================================

list2 =[50,25.50,'prashant']
list2.clear()
print(list2)

#=================================================================================

name = 'prashant'
print(name)
myname=list(name)#typecasting
print(myname)

#=================================================================================
mylist=[44,22,77,0,9,88]  #0,9,22,44,77,88
mylist.sort()
print(mylist)

mylist=[44,22,77,0,9,88]  #88, 77, 44, 22, 9, 0
mylist.sort()
mylist.sort(reverse=True)  #for descending order
print(mylist)

#=================================================================================
# ALICING --assgining one variable reference to another variable

mylist=[44,22,77,0,9,88]
newlist = mylist
print(id(mylist))
print(id(mylist))

mylist=[44,22,77,0,9,88]
for i in mylist:
    print(i)

#=================================================================================

# i/p =[0,1,4,0,2,5]
# o/p=[1,4,2,5,0,0]
#remove zero in the last/


mylist1=[0,1,4,0,2,5]
for i in mylist1:
    if i == 0:
        mylist1.remove(i)
        mylist1.append(i)
print(mylist1)

#=================================================================================

'''Find 2nd largest element
* Ques: find the 2nd largest element in an array
* Logic:
Samle Input: [7,3,9,2,8]
expected output: 2nd largest : 8
'''
list = [7,3,9,2,8]
list.sort()
print(list)
print(list[-2])

#=================================================================================
#MCQ

# 1) 

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)

#ans: ValueError--coz values are not adjusting till 60

# 2) 

a=[1,2,3,4,5]
print(a[3:0:-1])

#ans: [4, 3, 2]

# 3) 

arr= [[1,2,3,4],
      [4,5,6,7],
      [8,9,10,11],
      [12,13,14,15,]]
for i in range(0,4):
    print(arr[i].pop())

# 4)

arr = [1,2,3,4,5,6]
for i in range(1,6):
    arr[i - 1] = arr[i]

for i in range(0,6):
        print(arr[i], end =" ")

# 5) 

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
     if ls[0] == 'Guava':
          sum += 1
     if ls[1] == 'kiwi':
          sum +20
print(sum)

# ans: 22

# 6) 

 ''' find the intersection of three array
 Ques: find the common elements in three arrays
 Logic: Use 3 sets to keep track of common elements between the arrays.
 Sample input: [1,2,3], [2,3,4], [3,4,5]
 Expected output: [3]
 '''
A = [1,2,3]
B = [2,3,4]
C = [3,4,5]

for i in A:
     if i in B and i in C:
          print(i)

# 7)

mylist = []
N = int(input("Enter the value of N :"))#5
for i in range(N):
    val = int(input("Enter the value: "))
    mylist.append(val)
print(len(mylist))
sum =0 #5
for i in range(len(mylist)-1):#i=1
    if i+1 in range(len(mylist)):
        sum += abs(mylist[i]-mylist[i+1])#11 -7 =4
print(sum)