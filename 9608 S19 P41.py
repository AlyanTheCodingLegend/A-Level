class Player:
    def __init__(self,InputPlayerID):
        self.__Score=0
        self.__Category="Not Qualified"
        self.__PlayerID=InputPlayerID
    def GetScore(self):
        return self.__Score
    def GetCategory(self):
        return self.__Category
    def GetPlayerID(self):
        return self.__PlayerID
    def SetPlayerID(self): 
        playerID=''
        while len(playerID)<4 or len(playerID)>15:
            playerID=input('Please enter the Player ID: ')
        self.__PlayerID=playerID
    def SetScore(self,ScoreInput):
        if ScoreInput>=0 and ScoreInput<=150:
            self.__Score=ScoreInput
            return True
        else:
            print('Score inputted is invalid hence not stored.')
            return False
    def SetCategory(self):
        if self.__Score>120:
            self.__Category='Advanced'
        elif self.__Score>80 and self.__Score<=120:
            self.__Category='Intermediate'
        elif self.__Score>=50 and self.__Score<=80:
            self.__Category='Beginner'
        else:
            self.__Category='Not Qualified'


def CreatePlayer():
    playerID=input('Please enter the Player ID: ')
    scoreinput=int(input('Please enter the score: '))
    JoannePlayer=Player(playerID)
    JoannePlayer.SetScore(scoreinput)
    JoannePlayer.SetCategory()
    category=JoannePlayer.GetCategory()
    print(f'The object is of the category: {category}')

    