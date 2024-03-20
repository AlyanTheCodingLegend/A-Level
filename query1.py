import pickle

class Student:
    def __init__(self,name,address,classname):
        self.name=name
        self.address=address
        self.classname=classname

def AppendData(DataItem):
    binfile = open("students.dat", "ab")
    print("Enter the student details: ")
    DataItem.name=input("Enter student name: ")
    DataItem.address=input("Enter student address: ")
    DataItem.classname=input("Enter class name: ")

    pickle.dump(DataItem, binfile)

    binfile.close()


std1=Student("","","")

AppendData(std1)

