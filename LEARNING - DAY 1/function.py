# FUNCTION

def hello():
    print("hello world")

hello() #calling function
hello()

# INTERVIEW QUESTION

'''at a time is it possible to return multiple values in python?
ans: Yes — in Python, you can return multiple values at the same time from a function.'''

def arithmatic():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    sum = a+b
    sub = a-b
    div = a/b
    mul = a*b
    return sum, sub, div, mul

'''will this return tuple or list?
ans: tuple- as its values will not change.'''

# print(arithmatic())  # this will print answer in proper tuple format

# ans: Enter value of a: 5
#Enter value of b: 5
#(10, 0, 1.0, 25)

#or
result = arithmatic()
print("Arithmatic = ",result)

# Enter value of a: 5
# Enter value of b: 5
# Arithmatic =  (10, 0, 1.0, 25)

#=================================================================================================

#MCQ Question -- WIPRO
'''How many types of argument we pass in function?
Ans: There are 4 types of arguments:
1) Positional argument
2) Keyword argument
3) default argument
4) variable length argument / variable number of arguments'''

#------------------------------------------------------------------------------------------------------

# 1) Positional argument

# from left to right positions are fixed --
# Python matches arguments to parameters based on their order.

def arithmatic(a,b):  # a= 5, b = 5
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    sum = a+b
    sub = a-b
    div = a/b
    mul = a*b
    return sum, sub, div, mul

result = arithmatic(5,5)
print("Arithmatic = ",result) 
# ans: Enter value of a: 5
# Enter value of b: 5
# Arithmatic =  (10, 0, 1.0, 25)

#------------------------------------------------------------------------------------------------------

# 2) Keyword argument

# A keyword argument is an argument passed to a function using the parameter name.
#Instead of matching values by position, Python matches them by name.

# keyword name and parameter name must be same .

def credential(username, password):
    if username == password:
        print("login successfully")
    else:
        print("invalid credential")    

credential(username="admin", password="admin")  # calling function
# ans: login successfully

#------------------------------------------------------------------------------------------------------

# 3) Default argument

# A default argument means:
# If the user does not pass a value, Python automatically uses the default value.
# Syntax: def function(parameter = default_value):

def cityName(city="pune"):   # Here, city="pune" is called a default argument (or default parameter).
    print(city)

cityName("Nagpur")
cityName("Mumbai")
cityName()
# ans: Nagpur
# Mumbai
# pune

#------------------------------------------------------------------------------------------------------

# 4) variable length argument / variable number of argument

# can pass no of arguments at the same time

def cityName(*name):   # The * operator tells Python:
##“Collect all positional arguments into a tuple.”
    print(name)     

cityName("Nagpur", "delhi", "Mumbai", "pune")    
# ans: ('Nagpur', 'delhi', 'Mumbai', 'pune')

 # *name means:
# accept multiple values
# store them inside a tuple named name

#===================================================================================================================

# MODULARITY APPROACH IN FUNCTION

# In Python development, modularity means:
# Breaking a large program into smaller, independent, reusable functions/modules.

# Instead of writing everything in one big block:
# We divide the program into smaller functions.

import sys
def add():
    a = int(input("Enter Value of A: "))
    b = int(input("Enter Value of B: "))
    print(a+b)

def sub():
    a = int(input("Enter Value of A: "))
    b = int(input("Enter Value of B: "))
    print(a-b)

def div():
    a = int(input("Enter Value of A: "))
    b = int(input("Enter Value of B: "))
    print(a/b)

def mul():
    a = int(input("Enter Value of A: "))
    b = int(input("Enter Value of B: "))
    print(a*b)

while True:  # The loop will run infinite until you manually stop it or use break
    print("1. Addition")
    print("2. substraction")
    print("3. division")
    print("4. multiplication")
    print("5. exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add() # Calling Function
    elif choice == 2:
        sub() # Calling Function
    elif choice == 3:
        div() # Calling Function
    elif choice == 4:
        mul() # Calling Function
    elif choice == 5:
        sys.exit()  # or can use Break

# 1. Addition
# 2. substraction
# 3. division
# 4. multiplication
# 5. exit
# Enter your choice: 1
# Enter Value of A: 4
# Enter Value of B: 5
# 9
# 1. Addition
# 2. substraction
# 3. division
# 4. multiplication
# 5. exit
# Enter your choice: 2
# Enter Value of A: 4
# Enter Value of B: 5
# -1
# 1. Addition
# 2. substraction
# 3. division
# 4. multiplication
# 5. exit
# Enter your choice: 3
# Enter Value of A: 15
# Enter Value of B: 3
# 5.0
# 1. Addition
# 2. substraction
# 3. division
# 4. multiplication
# 5. exit
# Enter your choice: 4
# Enter Value of A: 3
# Enter Value of B: 4
# 12
# 1. Addition
# 2. substraction
# 3. division
# 4. multiplication
# 5. exit
# Enter your choice: 5
       