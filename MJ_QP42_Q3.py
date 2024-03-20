class TreasureChest:
    def __init__(self,q,a,p):
        self.__question=q #question as string
        self.__answer=a
        self.__points=p

def readData():
    try:
        file=open("TreasureChestData.txt","r")
        
        
        
        
        
        
        file.close()
    except FileNotFoundError:
        print("File not found")

