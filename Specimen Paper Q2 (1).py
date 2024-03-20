class HiddenBox:
    #__BoxName as String
    #__Creator as String
    #__DateHidden as String
    #__GameLocation as String
    #__LastFinds:ARRAY as String
    #__Active as Boolean
    def __init__(self,b,c,d,g):
        self.__BoxName=b 
        self.__Creator=c
        self.__DateHidden=d
        self.__GameLocation=g
        self.__LastFinds=[["" for column in range(2)] for row in range(10)]
        self.__Active=False
    def GetBoxName(self):
        return self.__BoxName
    def GetGameLocation(self):
        return self.__GameLocation

TheBoxes=[HiddenBox for i in range(10000)]   

def NewBox():
    global TheBoxes
    BoxName=input("Please enter the box name")
    Creator=input("Please enter the creator")
    DateHidden=input("Please enter the date hidden")
    GameLocation=input("Please enter the game location")
    TheBoxes.append(HiddenBox(BoxName,Creator,DateHidden,GameLocation))

NewBox()

class PuzzleBox(HiddenBox):
    def __init__(self,b,c,d,g,p,s):
        HiddenBox.__init__(b,c,d,g)
        self.__PuzzleText=p #PuzzleText as String
        self.__Solution=s #Solution as String








