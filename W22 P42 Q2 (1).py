class Character:
    def __init__(self,n,x,y):
        self.__Name=n #n as STRING
        self.__XCoordinate=x #x as INTEGER
        self.__YCoordinate=y #y as INTEGER
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate+=XChange
        self.__YCoordinate+=YChange

Characters=[Character(str,int,int) for i in range(10)]
filehandle=open("Characters.txt","r")
for i in range(10):
    name=filehandle.readline().strip()
    xcoord=int(filehandle.readline().strip())
    ycoord=int(filehandle.readline().strip())
    Characters[i]=Character(name,xcoord,ycoord)
filehandle.close()   

found=False
while found==False:
    inpname=input("Please enter a character:").lower()
    for j in range(10):
        temp=Characters[j].GetName().lower()
        if temp==inpname:
            index=j
            found=True
            break

inpname=inpname[0:1].upper()+inpname[1:]
letter=""
while letter!="W" and letter!="A" and letter!="S" and letter!="D":
    letter=(input("Please enter a letter W A S D:")).upper()
    if letter=="W":
        Characters[index].ChangePosition(0,1)
    elif letter=="A":
        Characters[index].ChangePosition(-1,0)    
    elif letter=="S":
        Characters[index].ChangePosition(0,-1)    
    elif letter=="D":
        Characters[index].ChangePosition(1,0)  
        
print(f"{inpname} has changed coordinates to X={Characters[index].GetX()} and Y={Characters[index].GetY()}")


     














