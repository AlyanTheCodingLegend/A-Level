class Course:
    def __init__(self,name,credithours,weightage):
        self.__name=name
        self.__credithours=credithours
        self.__weightage=weightage

class Student(Course):
    def __init__(self,weightage):
        Course.__init__(weightage)
        self.__name=""
        self.__coursestaken=[]
        self.__enrolldate=""
        self.__GPA=0
    def AddCourse(self,course):
        self.__coursestaken.append(course)
    def RegisterStudent(self,name,enrolldate):
        self.__name=name
        self.__enrolldate=enrolldate
    def CalculateGPA(self):  
        self.__GPA+=Course.__weightage    

class Department:
    def __init__(self,offeredcourses,principalname,stds):
        self.__courses=offeredcourses
        self.__principal=principalname
        self.__students=stds
    def IncStudent(self):
        self.__students+=1 
        
           


