'''A dictionary in Python is a collection used to store data in key-value pairs.

It is:

Mutable
Unordered (before Python 3.7)
Fast for searching
Uses keys instead of indexes'''

mydict = {
    101: "prashant",
    102: "ashish",
    "103": "mohini",
    "104": "trivani",
    101: "ashish",
    104: "ashish"
}
print(mydict)  # ans: {101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'trivani', 104: 'ashish'}

'''Dictionary keys must be unique.

If same key appears again:

old value gets replaced
latest value is kept
'''
# ------------------------------------------------------------------------------------------------------------------
# a = mydict[102]
# print(a) # ashish

#-------------------------------------------------------------------------------------------------------
# replace old value  by new value

# mydict[102] = "Peter"
# print(mydict) # ans : {101: 'ashish', 102: 'Peter', '103': 'mohini', '104': 'trivani', 104: 'ashish'}

#-------------------------------------------------------------------------------------------------------

# only print key x=0,1

# for x in mydict:
#     print(x)

 # ans : 101
# 102
# 103
# 104
# 104

#-------------------------------------------------------------------------------------------------------

# printing key and values both

# for x,y in mydict.items():
#     print(x,y)

# ans: 101 ashish
# 102 ashish
# 103 mohini
# 104 trivani
# 104 ashish

#-------------------------------------------------------------------------------------------------------

# adding a new key pair

# mydict["mobile_no"] = 454785594904
# print(mydict)

# ans: {101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'trivani', 104: 'ashish', 'mobile_no': 454785594904}

#-------------------------------------------------------------------------------------------------------

# mydict["Department"] = "management"
# print(mydict)

# ans: {101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'trivani', 104: 'ashish', 'mobile_no': 454785594904, 'Department': 'management'}

#-------------------------------------------------------------------------------------------------------

#imp: if we want to 

# mydict.pop(101)
# print(mydict)

#ans: {102: 'ashish', '103': 'mohini', '104': 'trivani', 104: 'ashish', 'mobile_no': 454785594904, 'Department': 'management'}

# pop() method remove pair by specific key name

#==========================================================================================================================================

#MCQ

# 1)

a = {(1,2):1, (2,3):2, (4,5):3}
     # key:value
print(a[4,5])   # ans: 3

# explanation : (1,2) is a key
'''1 is value

Similarly:

(4,5) → key
3 → value
Tuples can be used as dictionary keys because tuples are immutable.'''

# 2) 

a ={'a':1, 'b':2,'c':3}
print (a['a','b'])  # ans: KeyError

'''a['a','b'] becomes a[('a','b')], but the dictionary does not contain the 
tuple key ('a','b'), so Python raises KeyError.'''

a ={'a':1, 'b':2,'c':3}
print (a['a']) # ans: 1

# 3) 

arr ={}
arr[1] =1
arr['1'] = 2
arr[1] +=1
print(arr) # {1: 2, '1': 2}
sum = 0
for k in arr:
    sum += arr[k]
print(sum)      # 4

# 4) 

my_dict = {}
my_dict[1] =1
my_dict['1'] = 2
my_dict[1.0] = 4  # 1 and 1.0 are treated as SAME key ; 1 == 1.0 ; Output:True
print(my_dict)  # {1: 4, '1': 2}
sum = 0
for k in my_dict:
    sum+=my_dict[k]  # 4 + 2
print(sum)    # ans: 6

# 5) 

my_dict = {}
my_dict[(1,2,4)] = 8
       # key = value
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum = 0
for k in my_dict:
    sum +=my_dict[k]
print(sum)  # ans: 30
print(my_dict)    # {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}

# 5)

box = {}
jars = {}
crates = {}
box['biscuits'] = 1
box['cakes'] = 3
jars['jams'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box])) # ans: TypeError

# explanation: Dictionary cannot be used as another dictionary key."

box = {}
jars = {}
crates = {}
box['biscuits'] = 1
box['cakes'] = 3
jars['jams'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates['box']))  # nas: 2

# 6)

dict = {'c': 97, 'a': 96, 'b': 98}
for _ in sorted(dict):
    print(dict[_])  
# ans: 96
# 98
# 97

'''sorted(dict) sorts dictionary keys alphabetically as ['a', 'b', 'c'], and the loop prints their corresponding values: 96, 98, and 97.
'''

# 7)

rec ={"Name" : "Python", "Age": "20"}
r = rec.copy()
print(id(r) == id(rec)) # False
print(id(r)) # 3064924006464
print(id(rec)) # 3064923611648

# 8)

rec = {"Name" : "Python", "Age": "20", "Addr": "NJ", "Country" : "USA"}
id1 = id(rec)
print(id1)  # 2423293075968
del rec
rec = {"Name" : "Python", "Age": "20", "Addr": "NJ", "Country" : "USA"}
id2 = id(rec)
print(id2)  # 2423293075968
print(id1==id2)  # ans: True

#=============================================================================================

# find the key with the max value in a dictionary

#ques) write a function to find the key with the max value in a dictionary

# input: {"A" : 50, "B" :30, "C": 70}
# output: c

l = {"A": 50, "B": 30, "C": 70}
max_key = max(l, key=l.get)
print(max_key) # ans: C

#=============================================================================================

# find the key with min value
#ques) write a function to find the key with the min value in a dictionary
# input: {"X": 20, "Y": 10, "Z": 30}
# output: B

l = {"X": 20, "Y": 10, "Z": 30}
min_key = min(l, key=l.get)
print(min_key)  # ans: Y

#=============================================================================================

# ques) Write a function to count the frequency of elements in a list using a dictionary
#input: {1,2,2,3,4,3,5}
#output: {"1":1, "2":2, "3":2,"4":1,"5":1}

nums = [1,2,2,3,4,3,5]
freq = {}
for i in nums:
    freq[i] = nums.count(i)
print(freq) # {1: 1, 2: 2, 3: 2, 4: 1, 5: 1}