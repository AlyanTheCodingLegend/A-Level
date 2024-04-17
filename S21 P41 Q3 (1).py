#TYPE TreasureChest:
#   DECLARE question:STRING
#   DECLARE answer:INTEGER
#   DECLARE points:INTEGER
#ENDTYPE
class TreasureChest:
    def __init__(self,question,answer,points):
        self.__question=question
        self.__answer=answer
        self.__points=points
    def getQuestion(self):
        return self.__question    

arrayTreasure=[["" for i in range(3)]for j in range(5)]

def readData():
    #DECLARE arrayTreasure:ARRAY[0:4] OF TreasureChest
    global arrayTreasure
    try:
        global filehandle
        filehandle=open("TreasureChestData.txt", "r")
    except:
        print("File named TreasureChestData.txt was not found.") 
    for i in range(5):
        question=filehandle.readline()
        answer=filehandle.readline()
        points=filehandle.readline()
        arrayTreasure[i][0]=question
        arrayTreasure[i][1]=answer
        arrayTreasure[i][2]=points
    treasure1=TreasureChest(arrayTreasure[0][0],arrayTreasure[0][1],arrayTreasure[0][2])
    treasure2=TreasureChest(arrayTreasure[1][0],arrayTreasure[1][1],arrayTreasure[1][2])
    treasure3=TreasureChest(arrayTreasure[2][0],arrayTreasure[2][1],arrayTreasure[2][2])
    treasure4=TreasureChest(arrayTreasure[3][0],arrayTreasure[3][1],arrayTreasure[3][2])
    treasure5=TreasureChest(arrayTreasure[4][0],arrayTreasure[4][1],arrayTreasure[4][2])

def getQuestion(index):
    return arrayTreasure[index-1][0]

def checkAnswer(index, userans):
    if int(arrayTreasure[index-1][1])==int(userans):
        return True
    else:
        return False

def getPoints(index, attempts):
    if int(attempts)==1:
        return int(arrayTreasure[index-1][2])
    elif int(attempts)==2:
        return int(int(arrayTreasure[index-1][2])/2)
    elif int(attempts)==3 or int(attempts)==4:
        return int(int(arrayTreasure[index-1][2])/4)
    else:
        return 0
    
readData()
quesnum=int(input("Enter a question number between 1 and 5."))
flag=False
attempts=0
while flag==False:
    getQuestion(quesnum)
    userans=int(input("Please enter your answer to the question."))
    attempts += 1
    flag=checkAnswer(quesnum,userans)

point=getPoints(quesnum, attempts)
print(point)





