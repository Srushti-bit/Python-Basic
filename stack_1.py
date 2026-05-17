# TIME COMPLEXITY OF STACK
        
'''                   TC            SC
 1. Create stack -- O(1)          O(1)
 2. push -----------O(1)/O(n^2)   O(1)
 3. pop -------------O(1)         O(1)
  4. peek---------   O(1)         O(1)
  5. isEmpty----------O(1)        O(1)
  6. Delete entire Stack--O(1)    O(1)
'''


# TOWER OF HANOI

import time
class Tower:
    def __init__(self):
        print("WELCOME TO TPWER OF HANOI GAME")
        print()
        print("Given problem     A = [3,2,1]       B=[]       c=[]")
        print()
        print("Expected output   A =[]             B=[]       C=[3,2,1] ")
        self.A=[]
        self.B=[]
        self.C=[]

    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A=",self.A)
        print("Items in tower A\n")    

    def pass1(self):
        self.temp = self.A.pop(2)  # 2 is an indexno.
        self.C.append(self.temp)
        time.sleep(1)
        print("A=",self.A     ,"    ",   "B=",self.B  , "     ","C=",self.C)
        print("pass one completed============================\n")    

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(1)
        print("A=",self.A     ,"    ",   "B=",self.B  , "     ","C=",self.C)
        print("pass two completed============================\n")   

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(1)
        print("A=",self.A     ,"    ",   "B=",self.B  , "     ","C=",self.C)
        print("pass three completed============================\n")   

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print("A=",self.A     ,"    ",   "B=",self.B  , "     ","C=",self.C)
        print("pass four completed============================\n")     

    def pass5(self):
        self.temp = self.B.pop(1)
        self.C.append(self.temp)
        time.sleep(1)
        print("A=",self.A     ,"    ",   "B=",self.B  , "     ","C=",self.C)
        print("pass five completed============================\n")  

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print("A=",self.A     ,"    ",   "B=",self.B  , "     ","C=",self.C)
        print("pass six completed============================\n")            

    def pass7(self):
     self.temp = self.A.pop(1)
     self.C.append(self.temp)
     time.sleep(1)
     print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
     print("pass seven completed============================\n")

obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()