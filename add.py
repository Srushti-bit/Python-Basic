# pyhton is called as dynamically typed language

age = 33
pi = 3.14
name = "Srushti"
result = True
print(type(age))
print(type(pi))
print(type(name))
print(type(result))

print(id(age))
print(id(pi))
print(id(name))
print(id(result))

# why all fundamental datatypes are immutable ?

math = 50
chem = 50
phy = 50 

# All three can have the same ID because Python reuses immutable small integer objects.

print(id(math))
print(id(chem))
print(id(phy))


print(2+2)
print("2" + "2")
a = input ("Enter first number :")#2
b = input("Enter the second number : ")#2
print (a+b)

# input function by default accepts everything as a string.
# syntaxtically code is correct but logically it is wrong

# its solution is typecasting 
a = int(input("Enter first number :"))#2
b = int(input("Enter the second number : "))#2

print (a+b)

# int() used to convert in integer 3.14=int=3
print(int(3.14))#3
#print(int(10+5j)) --- cannot typcast complex values 
print(int(True))#1
#print(int("4.22"))
print(int(False))#0
#print(int("4/22"))
print(int("4"))#4

# we cannot convert complex value to int
#we can convert floating point value string to int
# cant convert string name to float
#=============================================================================================

# complex() used to convert 
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))

 #print(complex("name"))

print(complex(5,-3))
print(complex(True, False))

# The fundamental logic behind an object in Python is:

# Everything in Python is an object.

# Even numbers, strings, functions, and classes are objects.

#================================================================================================

# bool() is used to convert

print(bool(0)) #-- o always gives false 
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(False))
print(bool(True))
#print(bool("")) -- False
#print(bool("Srushti")) -- True

#===================================================================================================

# simple if 

a = int(input("Enter any single digit : "))
if a>0:
    print("Positive number")
if a<0:
     print("Negative number")
if a==0:
     print("Zero")     
        
# monday-sunday
# monday-fri - working
# sat-sund - weekend 

day = input("Enter day : ")

if day == "monday" or day == "MONDAY":
    print("Working day")

elif day == "tuesday" or day == "TUESDAY":
    print("Working day")    

elif day == "wednesday" or day == "WEDNESDAY":
    print("Working day")    

elif day == "thrusday" or day == "THRUSDAY":
    print("Working day")    

elif day == "friday" or day == "FRIDAY":
    print("Working day")            

elif day == "saturday" or day == "SATURDAY":
    print("Weekend")

elif day == "sunday" or day == "SUNDAY":
    print("Weekend")

    # OR

day = input("Enter day : ")
if day == "SATURDAY" or day == "saturday" or day == "SUNDAY" or day == "sunday":
    print("weekend")
else:
    print("working day")

#====================================================================================================================
# java and pythin follows UNICODE not ASCII code
# A = 65 : a = 97 : 0 = 48

per = 65
if per >=6:
    print("grade A")
elif per <=65 and per  >= 50:
    print("Grade B")
else:
    print("Fail")

#===============================================================================================

chr = ord(input("Enter any one character :")) #b
if chr >=65 and chr<=90:
    print("upper case")
elif chr >=97 and chr <=122:
    print("lower case")
elif chr >=48 and chr <=57:
    print("digit")        
else:
    print("special symbol")    

#======================================================================================================
# 1) Membership Operator -- used to check whether value is written or not

# i) in
# ii) not in    

# in python char and string comes under string 

name = "help4code"
print('p' not in name )

# 2) Identity Operator -- used for address comparison
  
  # i) is
  # ii) is not

math = 50 
chem = 50
print(math is chem)  # by id interpretor both have same address
# true

#======================================================================================================
# in pyhton we dont have any increment or decremnet symbol ( ++, --)
# for loop and while loop is called entry point

# for loop --if range is given then use for loop

# 1) 

for i in range(5): #i=0
    print(i)

# 2) 

for i in range(2,11): 
    print(i)

# 3) incement by 2

for i in range(2,11,2): 
    print(i)

# 4) decrement by 1

for i in range(5,0,-1): #i=5
    print(i)

# 5) table of 2

for i in range(1,11): #i=1
    print(i*2)

#  5.1) table of 2

for i in range(1,11): #i=1
    print(2*i)

# 6)  2      3       4        5     6 ...........10
    # 4      
    # 6
    # .
    # .
    # .
    # .
    # 20

#----------------------------------------------------------------------

#    11      12 ..................................20

for i in range(1,11): #i=1
    print(i*2, " ", i*3, " ", i*4, " ", i*5)

print("-----------------------")

for i in range(1,11):
        print(i*11, " ", i*12, " ", i*13, " ", i*14,)

# write a program to accept there paper marks and
# calculate total, %, and check if she/he is passed in all the subject
# so print pass else print fail
# 
# if % is greater than 65 and gender == "male" so he is eligible for placement or else not eligible      


sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))
total = sub1+sub2+sub3
percentage = total/3.0
print("Total Marks=", total)
print("Percentage=" , percentage)

if sub1 >=40 and sub2 >=40 and sub3 >=40:
    print("Pass")
else:
    print("Fail")   

gender = input("Enter your gender M/F: ")
if gender == "M" and percentage >=65:
    print("Eligible for placement") 
else:
    print("Not Eligible")    


#----------------------------------------------------------------------

for i in range(1,5): #i=3
    if i == 3:
        break
    print(i)

# break id not used in if else

for i in range(1,5): #i=4
    if i == 3:
        continue
    print(i)

#==========================================================
# output: 1 2 4  5 and 5 4 2 1
#
for i in range(1,6):
    if i==3:
        continue
    print(i)    

print()

for j in range(5,0,-1):
    if j==3:
        continue
    print(j)
print(i,"\t", j)    


# 2nd approach according to the given output

for i, j in zip(range(1, 6), range(5, 0, -1)):
    if i == 3 or j == 3:
        continue
    print(i, " ", j)

#==========================================================

num = 123  #321
# print(5/2)
# print(5//2)
a = num % 10
print( num % 10) #a =3
print( num)
num= num//10
print( num//10) # num = 12
b= num% 10 #b =2
c= num // 10 #c=1
rev = a*100 +b*10 + c*1 #300+20+1 = 321
print(rev)


num = 1234561
a = num % 10
num = num // 10
print(a) # 1
b = num % 10
num = num // 10
print(b)  # 6
c = num % 10
num = num // 10
print(c) # 5

d = num % 10
num = num // 10
num = 1234561
a = num % 10
num = num // 10
print(a) # 1
b = num % 10
num = num // 10
print(b)  # 6
c = num % 10
num = num // 10
print(d) # 4

e = num % 10
num = num // 10


f = num % 10
num = num // 10

g = num % 10

rev = a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 + g

print(rev)

#==========================================================

Amount = int(input("please Enter the amount for withdraw: "))
print("100 notes= " , (Amount//100))
print("50 notes= " , (Amount%100)//50)
print("20 notes= ",((Amount%100)%50)//20)
print("10 notes= ",(((Amount%100)%50)%20)//10)
print("10 notes= ",((((Amount%100)%50)%20)%10)//5)
