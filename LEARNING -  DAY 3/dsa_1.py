'''1. Data structure are different ways of organizing data on your computer, that can be used effectively

2. Set of steps to accomplish a task--Algorithm

video image compression algorithm ---are techniques used to reduce file size while trying to preserve visual quality.

They are used everywhere:
YouTube
Netflix
Instagram

3. Time Complexity --imp

  Best case
  Average Case
  Worst Case

4. types of O(n)

 imp: 1.  O(1) : constant time --Accessing specific element in an array
      2.  O(N) : linear time-- Loop through every elements--since it is visiting every elements
      3.  O(LogN) : Logarthmic -- find an elements in sorted array--since it is visiting only some elements -- example -> Binary Search is the best example for this .
      4. O(N^2) : Quadratic time --Looking at a every index in the array twice--this is avoided
      5. O(2^n) :Exponential time -- Double recursion in Fibonnaci

      imp-> which is efficent loop or recursion in terms of time and space complexity?
         ans:- Loops are generally more efficient than recursion because recursion adds extra overhead for every function call. 
         The main reason is:

        Recursion uses the call stack, while loops usually do not.
'''
# find the biggest number

def findbiggestNumber(sampleArray):           # O(1)
    biggestNumber  = sampleArray[0] # 5       # O(N)
    for index in range(1,len(sampleArray)):   # O(1)
        if sampleArray[index] > biggestNumber: # O(1)
            biggestNumber = sampleArray[index]  # O(1)
    print(biggestNumber)                        #O(1)

sampleArray = [5,7,9,2,3,4]                      # O(1)
findbiggestNumber(sampleArray)                   # O(1)
        
#====================================================================        

# O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(N) =  O(N) ---Final time complexity


'''
1. LINEAR SEARCH ---returns index value 
     Time complexity : O(N)
     space complexity : O(1)

* LINEAR SEARCH IN PYTHON

  LINEAR SEARCH PSEUDOCODE ---  must know pseudocode 
    1. Create a func with 2parameters which are an array and a value
    2. Loop through the array and check if the current array element is equal to the value
    3. If it is return the index at which the element is found
    4. If the value is never found return -1.
'''


def linearSearch(array,target):
    for i in range(0,len(array)):   # i =0    # O(N)
        if array[i] == target:                # O(1)
            return i     # returns index value   # O(N)
    return -1        # O(1)
array = [1,2,3,4,8,7,9]
target = 7    # search target value 7
result=linearSearch(array, target)
if result == -1:
    print("target value not found")
else:
    print("Element found at index ", result)    
    
#=============================================================================================================
# 
# Removing spaces from the string
# 
# 1.rstrip() ==>To remove spaces at the RHS
# 2.lstrip() ==>To remove spaces at the LHS
# 3. strip() ==>To remove spaces both side
# 
city=input("Enter your city Name: ")
scity=city.strip()
if scity=='Hyderabad':
    print("Hello Hyderabadi...Adab")
elif scity=='Chennai':
    print("Hello, Madrasi...Vanakkam")
elif scity=='Banglore':
    print("Hello Kannadiga....Shubhodaya")
else:
    print("your entered city is invalid")                

#=============================================================================================================

# ROW WISE MAX VALUE
#[[100, 198, 333, 323],
# [123, 232, 221, 111],
# [223, 565, 245, 764]]

mylist = [[100, 198, 333, 323],
[123, 232, 221, 111],
[223, 565, 245, 764]]
newlist = []
for i in range(3):
    j = 0
    max = mylist[i][j]
    for j in range(4):
        c_max = mylist[i][j]
        if max < c_max:
            max = c_max
    newlist.append(max)

print(newlist)     

#=============================================================================================================

# input = srushti*is*a*good*programmer
# output = ****srushtiisagoodprogrammer

name = 'srushti*is*a*good*programmer'
new_name = ''
val = ''
for i in name:
    if i != '*':
       new_name += i
    else:
        val+=i
print(new_name)        
print(str(val+new_name))           
    
#=============================================================================================================

# input = aaabbbbccceeeee
# output = a3b4c3e5

my_dict = {'a' : 3, 'b' : 4, 'c' : 3, 'e' : 5}  
new_dict = {}
for ch in my_dict:
    if ch in new_dict:
        new_dict[ch]+=1
    else:
        new_dict[ch] = my_dict[ch]    
print(new_dict)  
print(a['a'], b['b'], c['c'])


name = 'aaabbbbccceeeee'
newname = {}
for i in range(len(name)):
    key = name[i]
    count = 0
    for j in range(len(name)):
        if key == name[j]:
            count +=1
    newname[key] = count
# print(newname)
for i,j in newname.items():
    print(i,j,sep='',end='')           

    
    
            