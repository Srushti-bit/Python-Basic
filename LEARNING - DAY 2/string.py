name = "prahantjha" #this is a string
         #012345678910
print(name[0]) # p
print(name[1]) # r
print(name[-1]) # a
print(name[1:5]) # raha
print(name[0:5]) # praha
print(name[1:]) # rahantjha
print(name[:5]) # praha
print(name[:]) # prahantjha
print(name[1:8:2]) # rhnj
print(name[::-1])  # ahjtnaharp

#===================================================================================================

s ="Pyhton are High level programming Language"
print(s.lower()) # pyhton are high level programming language
print(s.upper()) # PYHTON ARE HIGH LEVEL PROGRAMMING LANGUAGE
print(s.swapcase()) # pYHTON ARE hIGH LEVEL PROGRAMMING lANGUAGE
print(s.title())  # Pyhton Are High Level Programming Language
print(s.capitalize()) # Pyhton are high level programming language

#===================================================================================================
# Format Function

name = "srushti"
sal = 5000
age = 28
print("{} sal is {} age is {}".format(name,sal,age))  # srushti sal is 5000 age is 28
print("{0} sal is {1} age is {2}".format(name,sal,age)) # srushti sal is 5000 age is 28
print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age)) # srushti sal is 5000 age is 28
A=1
print(f"{A} is a good boy")  # 1 is a good boy

#===================================================================================================

name = "srushti"
for i in name: # i=0 
    print(i) 

#===================================================================================================
#i/p = srushti
#o/p = sruhti
#WAP to remove duplicate chr

name = "srushti"
newname = ""
#print(type(newname))
for i in name:
    if i not in newname:
        newname += i
print(newname)      

#===================================================================================================
#i/p = srushti

#WAP to reverse the string using loop

name = "srushti"
newname = ""
N = len(name)
for i in range(N-1,-1,-1):
    newname += name[i]
print(newname)

#===================================================================================================
# CHECK FOR PALINDROME

# ques) WAP to check if a given string is a palindrome
# logic) use loops to compare chr from the strt and end of the string
# sample: "racecar"
# output: paliindrome

name = "racecar"
print(name)
print(name [::-1])
if name ==name[::-1]:
    print("pallindrome")
else:
    print("Not a Pallindrome")    

#===================================================================================================

#check for palindrome
# name = "racecar"
name = "help4code"
print(name)
print(name[::-1])
if name == name[::-1]:
    print("palindrome")
else:
    print("Not palindrome")

#===================================================================================================
#count vowels and consonants
#wAP to count the number of vowels and consonants in a given string
#sample input = "hello"

vowels =['a','e','i','o','u']
name = "hello"
cons =0 #1
vow =0#
for i in name:#i=4:o
    if i in vowels:
        vow += 1
    else:
        cons +=1
print("consonent =",cons)
print("vow ",vow)

#=========================================================================
#check for anagram
# WAP to check if two string are anagrams of each other.
# logic: check if the character counts in both strings are the same
# sample input: "listen" and "silent"
# output: Anagram




#===========================================================================
#count words in a string
#WAP to count the number of words in a string
# logic: use loops to count spaces and words
# sample input "THis is a sentence"
# output: 4




#===========================================================================

a = 50
b=30
c=20
d=10
print((a+b)*c/d)

#===========================================================================

s = "this is a test"
print(s.title())

#===========================================================================

print('prashantjha777' .isalnum())#True
print('prashantjha'.isalpha())#True
print('777'.isdigit())
print('sdsdsdsd'.islower())
print(''.islower())
print('PRASHANT'.isupper())
print('My Name Is Prashant'.istitle())
print(''.istitle())
print(''.isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))

print("Prashant".find("r"))
print("Prashant".index("r"))
print("Prashant jha".count("a"))

#===========================================================================

    