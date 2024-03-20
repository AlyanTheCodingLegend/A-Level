class Card:
    def __init__(self,number,colour):
        self.__numberP=number #INTEGER 
        self.__colourP=colour #STRING
    def GetNumber(self):
        return self.__numberP
    def GetColour(self):
        return self.__colourP

#DECLARE CardArray:ARRAY[0:29] OF Card#
CardArray=[Card(0,"") for i in range(30)]
filehandle=open("CardValues.txt","r")
for i in range(30):
    CardArray[i].GetNumber=filehandle.readline()
    CardArray[i].GetColour=filehandle.readline()

selectedCards=[0 for i in range(30)]

def ChooseCard():
    index=0
    flag=False
    selected=False
    ind=0
    stored=False
    while flag==False:
        while selected==False:
            while (index<1 or index>30):
                index=int(input("Please enter the index of the card to be chosen: "))
            for i in range(30):
                if selectedCards[i]==index:
                    selected=True
            
            if selected==False:
                while stored==False:
                    if selectedCards[ind]==0:
                        selectedCards[ind]=index
                        stored=True
                    ind+=1
        flag=True        
    return index        

Player1=[Card(0,"") for i in range(4)]
for i in range(4):
    index=ChooseCard()
    Player1[i]=CardArray[index-1]
    print(str(Player1[i].GetNumber)+" "+Player1[i].GetColour)




            
