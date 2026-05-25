# '''
# REGULAR EXPRESSION:

#   1) used to develop the digital circuit
#   2) used to develop the compiler and interpreter
#   3) used to develop the communication protocol like TCP/IP etc
#   4) used to develop the validation logic
#   5) used to develop the pattern matching and searching application like ctrl f
# '''

# import re
# count = 0
# pattern = re.compile("python")
# print(pattern)

# matcher = pattern.finditer("A function in python is defined by a def statement. " \
# "python the general syntac looks like this: def functiom-name(parameter list): statement., " \
# "i.e thr function body. the parameter python list consists of none or more parameters")
# print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.group())
# print("the number of occurrence: ",count)   

# # ans:
# # re.compile('python')
# # <callable_iterator object at 0x0000021CDA605F60>
# # 14 ... python
# # 52 ... python
# # 179 ... python
# # the number of occurrence:  3

# #==========================================================================================================================

# import re
# count = 0
# matcher = re.finditer("Hi", "HiHiHi")

# for i in matcher:
#     count +=1
#     print(i.start(),".....",i.end(),"...",i.group())
# print("the num of occurences: ",count)

# # ans:
# 0 ..... 2 ... Hi
# 2 ..... 4 ... Hi
# 4 ..... 6 ... Hi

#=========================================================================================

import re
obj = input("enter any character: ")
objmatch = re.finditer(obj,"a7b @k9z")
#print(objmatch)
for match in objmatch:
    print(match.start(),"...",match.end(),"....",match.group())

#======================================================================================================
# MATCH FUNCTION --Checks string at the beginning 

import re
a = input("enter string to perform match operation: ")
mtch = re.match(a, "python is very imp language")
print(mtch)
if mtch != None:
    print("match found at beginning level")
    print(mtch.start()," ",mtch.end())

else:
    print("there is no matching at beginning level")    

#============================================================================================
# 
# FULL MATCH--full stirng should match
#eg: password 

import re
a = input("enter string to perform match operation: ")
mtch = re.fullmatch(a, "pythonisveryimp")
print(mtch)
if mtch != None:
    print("match found")
    print(mtch.start()," ",mtch.end())

else:
    print("full match not found")       

# eg
# WA python program to check whether the given mail is valid gmail id or not?
# 
import re
s = input("Enter mail id: ")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
if m!=None:
    print("valid ")
else:
    print("invalid")           

#or 
import re
s = input("Enter mail id: ")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@rbunagpur[.]in", s)
if m!=None:
    print("valid ")
else:
    print("invalid")           

#WAP to check valid mobile no.
# 
import re
mo = input("enter mobile no: ")
obj = re.fullmatch("[0-5]\d{9}",mo)
if obj!=None:
    print("valid")
else:
    print("invalid")        

#-----------------------------------------------------------------------------------------------------------------------

import re
a = input("enter string to perform match operation: ")
mtch = re.search(a, "python is very imp")
print(mtch)
if mtch != None:
    print("match found")
    print(mtch.start()," ",mtch.end(), " ", mtch.group())

else:
    print("match not found")       

#---------------------------------------------------------------------------------------------------------------------

import re
a = input("enter string to perform match operation: ")
mtch = re.findall('[A-Z]' ".,mfd,dv,lksd@$Wvflo3DNSJDN048mvmkck")
print(mtch)

import re
obj = re.sub('[a-z]', '*','2345 ABCD habc deff')
print(obj)

#==============================================================================================================

import re
f1 = open("input.txt","r")
# f2 = open("input.txt","w")
pattern ="""A function in python is defined by a def statement. 
python the general syntac looks like this: def function-name(parameter list): statement., 
i.e thr function body. the parameter python list consists of none or more parameters"""
text = f1.read()
result = re.fullmatch(pattern, text)
if result:
    print("Matched")
else:
    print("Not Matched")

f1.close()
