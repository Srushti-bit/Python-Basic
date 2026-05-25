'''
There are 3 types of varibales

1) Instant Variables - 
  
Instance variables are declared inside the constructor using self.
They store object-specific data.
Their values change from object to object.
Every object gets its own separate copy of instance variables.
Modifying one object’s variables does not affect another object.

They are accessed using:
object_name.variable_name
'''
 # instant variable depends on state of obj
class New:
    def __init__(self):
        self.a = 10
Obj1 = New()        
Obj2 = New()    
Obj3 = New()    
Obj1.a = 20

print(Obj1.a)
print(Obj2.a)
print(Obj3.a)

#=================================================================================

''''
2) Static Variables - 

Static variables belong to the class, not to objects.
They are declared inside the class but outside methods.
All objects share the same copy of static variables.
If the value changes, it affects all objects.
They are used to store common data.

They can be accessed using:
ClassName.variable_name
'''
# static variable does not depend on obj
class New():
    a = 10
    def __init__(self):
        self.name = "srushti"  

Obj1 = New()        
Obj2 = New()   
Obj3 = New()  
New.a = 50  
    
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)    

# ans:                        
# 50
# 50
# 50

#--------------------------------------------------------------------------------------------------------
  # difference between instance and static variable  ---INTERVIEW QUES

class College:
    collegename = "Modern College"
    def __init__(self):
        self.studentname = "prashant" #instance variable(3 separate memory)
principal = College()  #object creation
teacher = College()
accountant = College()
print("principal = ", principal.collegename,"...",principal.studentname)
print("teacher = ", teacher.collegename,"...",teacher.studentname)     
print("accountant = ", accountant.collegename,"...",accountant.studentname)  
College.collegename = 'HBD'
principal.studentname = "Srushti Lohakare"
print("principal = ", principal.collegename,"|",principal.studentname)
print("principal = ", principal.collegename,"|",principal.studentname)
print("principal = ", principal.collegename,"|",principal.studentname)