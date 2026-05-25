import logging
logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
try:
    a = int(input("enter 1st integer no : "))
    b = int(input("enter 2nd integer no : "))
    print(a/b)
except(ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging Level is set up. Check 'newfile.txt' for log details.")        

#=========================================================================================================

import csv
f = open("employee.csv", 'a')
a = csv.writer(f)
# a.writerow(["EmpID", "EMP Name", "EMP Age"])
empid = int(input("enter your empid: "))
empName = int(input("enter emp name: "))
age = int(input("enter emp age: "))
a.writerow([empid, empName, age])
print("file has created")

Import csv
f = open("employee.csv", 'a')
a = csv.writer(f)

