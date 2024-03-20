class Player:
    def __init__(self):
        self.__score=0 #score as Integer
        self.__category="Beginner" #category as String
        self.__PlayerID="" #PlayerID as String
    def Assign(self,score,category,PlayerID):
        self.__score=score
        self.__category=category
        self.__PlayerID=PlayerID
    def SetCategory(self,category):
        self.__category=category
    def GetCategory(self):
        return self.__category
    def GetPlayerID(self):
        return self.__PlayerID
    def GetScore(self):
        return self.__score            
    def PrintData(self):
        print(f'The score of the player is {self.GetScore()}')
        print(f'The category of the player is {self.GetCategory()}')
        print(f'The PlayerID of the player is {self.GetPlayerID()}')
        
class BasketBallPlayer(Player):
    def __init__(self):
        self.__Fouls=0 #Fouls as Integer
    def Assign(self,Fouls,score,category,PlayerID):
        self.__score=score
        self.__category=category
        self.__PlayerID=PlayerID
        self.__Fouls=Fouls 
    def GetFouls(self):
        return self.__Fouls  
    def PrintData(self):
        print(f'The score of the player is {self.GetScore()}')
        print(f'The category of the player is {self.GetCategory()}')
        print(f'The PlayerID of the player is {self.GetPlayerID()}')
        print(f'The fouls of the player are {self.GetFouls()}')      

def AssignNow(Fouls,score,category,PlayerID):
    global HamidPlayer
    HamidPlayer=BasketBallPlayer()
    HamidPlayer.Assign(Fouls,score,category,PlayerID)

def PrintDetails(player):
    player.PrintData()

