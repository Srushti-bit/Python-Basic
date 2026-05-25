#object creation in Python

class Name:
    age = 30
    def display(self):
        print("Hello World")

obj = Name()
print(obj.age)
obj.display()

#=================================================================================================

#object creation with Constructor
class Student:
    def __init__(self):
        self.name = "srushti"
        self.age = 22

    def display(self):
        print("Name= ", self.name)
        print("Age= ",self.age)

stuObj = Student()
print(stuObj)

#----------------------------------------------------------------------------

class Message:
    def __init__(self):  #Constructor
         self.name = "srushti"

    def shows(self):
        print("Class program")
        
obj = Message()    
obj.shows()
obj2 = Message()    

#----------------------------------------------------------------------------

class StudentInfo:
    def __init__(self, name, age, roll_no):  #Constructor
       self.Name = name
       self.Age = age
       self.RollNo = roll_no


    def displayStudentInfo(self):
        print("Name= ",self.Name)
        print("Age= ",self.age)
        print("RollNo= ",self.roll_no)
        
studentObj = StudentInfo("Srushti", 22)
studentObj = StudentInfo("Srushti", 22)
