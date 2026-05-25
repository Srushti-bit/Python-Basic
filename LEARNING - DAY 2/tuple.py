'''A tuple in Python is a collection used to store multiple items in a single variable.

It is:

Ordered
Immutable
Allows duplicate values
Faster than list
Uses less memory'''

# INTERVIEW QUES
# Diff between list and tuple in detail

'''In Python, lists and tuples both store collections of data, but their applications differ based on mutability.

Lists are preferred in applications where data manipulation is required frequently, such as inventory systems, live dashboards, or task management applications.

Tuples are preferred for fixed data structures like API responses, database records, coordinates, and dictionary keys because they provide better performance and data integrity.

Since tuples are immutable, they are also safer in multi-threaded and large-scale applications.'''

mytuple = ("prashant", "Ashish", "Rahul", "sandip" "Komal", "ankush", "rajesh", 23,3,15,77,"sandip")
print(mytuple)
print(type(mytuple))

# mytuple[2] = "sunil" # immutable
# print(mytuple)

#==========================================================================================================
#MCQ 
# 1)

init_tuple = ()
print(init_tuple.__len__()) # ans: 0

# 2) 

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print(init_tuple_a == init_tuple_b)  # ans: True

# 3)

init_tuple_a = '1','2'
init_tuple_b = ('3','4')
print(init_tuple_a + init_tuple_b)  # ans: ('1', '2', '3', '4')

# 4)

l = [1,2,3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)   # ans: ()
#explanation: The code:

# finds list length → 3
# finds first element of reversed list → 3
# subtracts them → 0
# repeats tuple 0 times
# so output is an empty tuple ()

# 5)

init_tuple = ('Python',)*3
print(type(init_tuple))  # ans: <class 'tuple'>

init_tuple = ('Python')*3  # removed comma
print(type(init_tuple))  # ans: <class 'str'>

# 6)

init_tuple = (1,) * 3  #  l = [1,1,1]   ; l[0] = 2  ; [2,1,1] ; t = (1,1,1) ;t[0] = 2 ; TypeError
print(l)
init_tuple[0] = 2
print(init_tuple)   # ans: 'tuple' object does not support item assignment

# 7) 

init_tuple = ((1,2),) *7
#print(init_tuple)
print(len(init_tuple[3:8]))

