PlayerInfo=[[0 for i in range(2)]for j in range(10)]
filehandle=open("HighScore.txt", "r")
def ReadHighScores():
    for i in range(10):
        name=filehandle.readline().strip()
        PlayerInfo[i][0]=name
        score=filehandle.readline().strip()
        PlayerInfo[i][1]=score 
    

def OutputHighScores():
    for i in range(10):
        name=PlayerInfo[i][0]
        score=PlayerInfo[i][1]
        details=name+" "+score
        print(details,end=" ")

ReadHighScores()
OutputHighScores()

name=""
while len(name)!=3:
     name=input("Please enter a 3-character player name.")
     name=name.upper()

score=0
while score<1 or score>100000:
     score=int(input("Please enter the score of the player which must be between 1 and 100000 inclusive."))

def NewList(name,score):
    lowscore=int(100001)
    for i in range(10):
        temp=int(PlayerInfo[i][1])
        if int(lowscore)>int(temp):
            lowscore=PlayerInfo[i][1]
            index=i
    if int(lowscore)<int(score):
        PlayerInfo[index][0]=name
        PlayerInfo[index][1]=score
        
print(PlayerInfo)
NewList(name,score)
print(PlayerInfo)

def WriteTopTen():
    filehandle1=open("NewHighScore.txt", "w")
    for i in range(10):
        names=str(PlayerInfo[i][0])+"\n"
        scores=str(PlayerInfo[i][1])+"\n"
        filehandle1.write(names)
        filehandle1.write(scores)

WriteTopTen()