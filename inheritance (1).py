import datetime
#base class
class libraryItem:
    # constructor
    def __init__(self, t, c, i):
        self.__title = t
        self.__creator = c
        self.__itemID = i
        self.__onLoan = False
        #duedate is defined as DATE
        self.__duedate = datetime.date.today()
    
    duration = 1
    def borrowing(self):
        duration = 5
        self.__onLoan = True
        self.__dueDate = datetime.date.today()+datetime.timedelta(duration)
    
    def returning(self):
        self.__onLoan = False

#printDetails 
    def printDetails(self):
        print("Title:", self.__title)
        print("Creator:", self.__creator)
        print("Item ID:", self.__itemID)
        print("On loan:", self.__onLoan)
        print("Due Date:", self.__dueDate)

#Getter statements
    def getTitle(self):
        return self.__title

    def getCreator(self):
        return self.__creator
    
    def getItemID(self):
        return self.__itemID
    
    def getDueDate(self):
        return self.__dueDate

    def getOnLoan(self):
        return self.__onLoan
    
class book(libraryItem):
    #constructor
    def __init__(self, t, c, i):
        libraryItem.__init__(self, t, c, i)
        self.__isRequested = False

    def getIsRequested(self):
        return self.__isRequested

    def setIsRequested(self, r):
        self.__isRequested = r
    
#polymorphism: the method behaves differently for various classes of the library
    def printDetails(self):
        libraryItem.printDetails(self)
        print("Is Requested:", self.__isRequested)


myBook = book("Harry Potter", "JK Rowling", 123)
myBook.borrowing()
# calls subclass method
myBook.printDetails()

class CD(libraryItem):
    #constructor
    def __init__(self, t, c, i):
        libraryItem.__init__(self, t, c, i)
        self.__genre = " "
    
    def getGenre(self):
        return self.__genre

    def setGenre(self, g):
        self.__genre = g

myCd = CD("All queit on the western front", "Edward Berger", 285)
myCd.borrowing()
myCd.printDetails()


from random import randint
import pickle

x=randint(1,50)
print(x)

