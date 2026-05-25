''' 
Static Method:

A method that:
belongs to the class
does NOT use self
does NOT access instance variables directly
'''



class Student:
    #by using class name we can access static method
    @staticmethod #decorator
    def get_personal_detail(firstname, lastname):
        print("ypur personal detail= ",firstname, lastname)

    @staticmethod
    def contact_detail(mobile_no, rollno):
        print("your contact detail= ", mobile_no, rollno)

Student.get_personal_detail("srushti", "lohakare")
Student.contact_detail(945849598349, 1001)  

'''
garbage Collection--  deletion of unused memory
resource deallocate-- destructor

(connect garbage collection with destructor in interview)
'''

''''
inheritance -- 
 1)single 
 2) multiple
'''

#single level inheritance

class College:
    def college_name(self):
        print("modern college")

class Student(College):
    def student_info(self):
        print("Name: Srushti Lohakare")
        print("branch: MCA")

obj = Student()  #object create child class
obj.college_name()
obj.student_info()                

#============================================================

# multilevel inheritance

class College:
    def college_name(self):
        print("modern college")

class Student(College):
    def student_info(self):
        print("Name: Srushti Lohakare")
        print("branch: MCA")

obj = Student()  #object create child class
obj.college_name()
obj.student_info()                

class Exam(Student):
    def subject(self):
        print("Subject1: Design Engineering")
        print("Subject2: Math")
        print("Subject3: C-language")
obj = Exam()
obj.college_name() 
obj.subject()       
        
# multiple inheritance

class SubjMarks:
    math = int(input("enter paper marks of math: "))        
    math = int(input("enter paper marks of design engg: "))  
    math = int(input("enter paper marks of C language: "))

class Practmarks:
    cpract = int(input("Enter practicals marks of c language: "))

class Result(SubjMarks, Practmarks):
    print("if student pass in both = subject and practical paper then pass")
    def total(self):
        if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
            print("pass")
        else:
            print("fail")
obj = Result()
obj.total()                
      

''''
compile time overloading:
python only supports operator overloading

runtime overloading:


'''      

class rbi:
    def home_loan(self):
        print("Home loan ROI = 8%")

    def education_loan(self):
        print("Education loan = 9%")

class sbi(rbi):
    def education_loan(self):
        print("education loan = 10%")
        #super().education_loan()              
obj = sbi()
obj.education_loan()    

#===============================================================================================================
#constructor overridding

class rbi:
    def __init__(self):
        print("parent class constructor")

class sbi(rbi):
    def __init__(self):
        print("child class constructor")
             
obj = sbi()
