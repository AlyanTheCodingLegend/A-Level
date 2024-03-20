class Card:
    def __init__(self,Number,Colour):
        self.__NumberP=Number #DECLARE Number:INTEGER 
        self.__ColourP=Colour #DECLARE Colour:INTEGER
    def GetNumber(self):
        return self.__NumberP
    def GetColour(self):
        return self.__ColourP
    
Card1=Card(1,"red") 
Card2=Card(2,"red") 
Card3=Card(3,"red") 
Card4=Card(4,"red") 
Card5=Card(5,"red") 
Card6=Card(1,"blue")    
Card7=Card(2,"blue")    
Card8=Card(3,"blue")
Card9=Card(4,"blue")    
Card10=Card(5,"blue")
Card11=Card(1,"yellow")
Card12=Card(2,"yellow")
Card13=Card(3,"yellow")
Card14=Card(4,"yellow")
Card15=Card(5,"yellow")

class Hand:
    def __init__(self,card1,card2,card3,card4,card5,Cards):
        Cards[0]=card1
        Cards[1]=card2
        Cards[2]=card3
        Cards[3]=card4
        Cards[4]=card5
        self.__Cards=Cards
        self.__FirstCard=0
        self.__NumberCards=5
    def GetCard(self,index):
        return self.__Cards[index]
     
Player1=Hand(Card1,Card2,Card3,Card4,Card11,[Card(0,"") for i in range(10)])
Player2=Hand(Card12,Card13,Card14,Card15,Card6,[Card(0,"") for i in range(10)])

def CalculateValue(playerhand):
    score=0
    for i in range(5):
        if playerhand.GetCard(i).GetColour()=="red":
            score+=5
        elif playerhand.GetCard(i).GetColour()=="blue":
            score+=10
        else:
            score+=15
        score+=playerhand.GetCard(i).GetNumber()
    return int(score)        

score1=CalculateValue(Player1)
score2=CalculateValue(Player2)
if score1==score2:
    print("The game was a draw.")
elif score1>score2:
    print("Player 1 won the game.")
else:
    print("Player 2 won the game.")    

print(score1)
print(score2)
    





