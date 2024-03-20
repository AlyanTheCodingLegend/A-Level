import datetime

class libraryitem:
    def __init__(self, t, a, i):
        self.__title = t
        self.__author__artist = a 
        self.__itemid = i
        self.__onloan = False
        self.__duedate = datetime.date.today()
    def gettitle(self):
        return (self.__title)
    def borrowing(self):
        self.__onloan=True
        self.__duedate = self.__duedate+datetime.timedelta(weeks=3)
    def returning(self):
        self.onloan = False
    def printdetails(self):
        print(self.__title, ',' , self.__author__artist, ',')
        print(self.__itemid, ',', self.__onloan, ',', self.__duedate)

class book(libraryitem):
    def __init__(self, t, a, i):
        libraryitem.__init__(self,t,a,i)
        self.__isrequested = False
        self.__requestedby = 0
    def getisrequested(self):
        return (self.__isrequested)
    def setisrequested(self):
        self.__isrequested = True

class cd(libraryitem):
    def __init__(self, t, a, i):
        libraryitem.__init__(self, t, a, i)
        self.__genre = ""
    def getgenre(self):
        return (self.__genre)
    def setgenre(self, g):
        self.__genre = g


thisbook = book("title", "author", "itemid")
thiscd = cd("title", "artist", "itemid")
