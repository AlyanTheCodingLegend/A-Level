# Containment is a relationship in which one classs has a component that is of another class
# somewhat similar to one to many relationships in a database
# delegation of one class to another class is called containment

#base class
class lesson:
    #constructor
    def __init__(self, t, d, r):
        self.__lessontitle = t
        self.__duration = d
        self.__requiresLab = r
    
    def outputLessonDetails(self):
        print("Lesson Title: {0}, Duration in mins: {1}, Requires Lab: {2}".format(self.__lessontitle, self.__duration, self.__requiresLab) ) # formatted string 
                                                                                         
class assessment:
    def __init__(self, t, m):
        self.__assessmentTitle = t
        self.__maxmarks = m

    def outputAssessmentDetails(self):
        print("Assesment Marks: {0}, Max Marks: {1}".format(self.__assessmentTitle , self.__maxmarks))

class course:
    def __init__ (self, t, m):
        self.__courseTitle = t
        self.__maxStudents = m
        self.__numberOfLessons = 0
        self.__courseLesson = []
        self.__courseAssessment = assessment(t,m) #calling of one class into another class so as to use the attributes of that class in this class 

    def outputCourseDetails(self):
        print("Course Title: {0}, Max Students: {1}, Number Of Lessons: {2}".format(self.__courseTitle, self.__maxStudents, self.__numberOfLessons))
    
        for i in range(self.__numberOfLessons):                               # for loop increment the the index value in courseLesson array 
            print(self.__courseLesson[i].outputLessonDetails())                
        self.__courseAssessment.outputAssessmentDetails()
    
    def addLesson(self, t, d, r):
        self.__courseLesson.append(lesson(t,d,r))
        self.__numberOfLessons += 1
    
    def addAssessment(self, t, m):
        self.__courseAssessment = assessment(t, m)

myCourse = course("Computer Science", 25) #sets up a new course
myCourse.addLesson("Containment", 50, True)
myCourse.addLesson("OOP", 200, True)
myCourse.addAssessment("P4 test", 75) #addition of an assignment
#check it all works
myCourse.outputCourseDetails()