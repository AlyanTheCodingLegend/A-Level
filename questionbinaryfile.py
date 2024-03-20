import datetime
import pickle

class Employee:
    def __init__(self, fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.dateEmployed=datetime.datetime.now()

emp1 = Employee("Alyan", "Ahmed", 82321)

firstname=input("Please enter first name of the employee: ")
lastname=input("Please enter second name: ")

emp1.fname=firstname
emp1.lname=lastname

emp_file = open("niceEmployeeFile.dat", "wb+")

pickle.dump(emp1, emp_file) # serialization

emp_rec=pickle.load(emp_file)
# record could be customised in any way


emp_file.close()

def appendData(employee_record):
    emp_file = open("niceEmployeeFile.dat", "wb+")

    pickle.dump(emp1, emp_file) # serialization
    emp_file.close()

# break = breaks from the loop
# return = exits from the function
    
def search(id):
    try:
        emp_file=open("jandjsand.dat","rb")
        while True:
            try:
                emp=pickle.load(emp_file)
                try:
                    identify=float(emp.id)
                except ValueError:
                    break
                if emp.id==id:
                    print("Yeh lo details")
                    break
            except ZeroDivisionError:
                print("infinity")
                break

        emp_file.close()

    except IOError:
        print("File not found")         

    # file not found error, file ends, value error       

textfile = open("blabla.txt", "a+")

textfile.readline()

str = "   alyan  \n"
str.strip()



