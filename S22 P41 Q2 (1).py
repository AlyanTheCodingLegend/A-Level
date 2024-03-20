class Balloon:
    def __init__(self,Colour,DefenceItem):
        self.__Health=100 #INTEGER 
        self.__ColourP=Colour #STRING
        self.__DefenceItemP=DefenceItem #STRING
    
    def GetDefenceItem(self):
        return self.__DefenceItemP
    
    def ChangeHealth(self,change):
        self.__Health += int(change)
    
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
            
defenceitem=input("Please enter a defence item: ")
colour=input("Please enter a colour: ")
Balloon1=Balloon(colour,defenceitem)

def Defend(Balloon):
    strength=int(input("Please enter the strength of the opponent: "))
    Balloon.ChangeHealth(-strength)
    print (Balloon.GetDefenceItem())
    if Balloon.CheckHealth()==True:
        print("The object has no health remaining.")
    else:
        print("The object has health remaining.")
    return Balloon
        
Defend(Balloon1)


        
