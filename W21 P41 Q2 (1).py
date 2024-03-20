#TYPE Picture:
#   DECLARE Description:STRING
#   DECLARE Width:INTEGER
#   DECLARE Height:INTEGER
#   DECLARE FrameColour:STRING
#ENDTYPE

class Picture:
    def __init__(self,Description,Width,Height,FrameColour):
        self.__picDescription=Description
        self.__picWidth=Width
        self.__picHeight=Height
        self.__picFrameColour=FrameColour
    def GetDescription(self):
        return self.__picDescription
    def GetHeight(self):
        return self.__picHeight
    def GetWidth(self):
        return self.__picWidth
    def GetColour(self):
        return self.__picFrameColour
    def SetDiscription(self,description):
        self.__picDescription=description

#DECLARE PicArray:ARRAY[0:99] OF Picture
global PicArray
PicArray=[Picture("",0,0,"") for i in range(100)]

def ReadData(PicArray):
    try:
        filehandle=open("Pictures.txt","r")
        i=0
        desc=filehandle.readline().strip().lower()
        while len(desc)!=0:
            width=int(filehandle.readline().strip())
            height=int(filehandle.readline().strip())
            framecol=filehandle.readline().strip().lower()
            PicArray[i]=Picture(desc,width,height,framecol)
            desc=filehandle.readline().strip().lower()
            i+=1       
        filehandle.close()     
        return i,PicArray
    except IOError:
        print("File named Pictures.txt was not found.")

count,PicArray=ReadData(PicArray)

colofframe=str(input("Please enter the colour of the frame.").lower())
maxwidth=int(input("Please enter the maximum width of the picture."))
maxheight=int(input("Please enter the maximum height of the picture."))

for i in range(count):
    if maxheight>=PicArray[i].GetHeight() and maxwidth>=PicArray[i].GetWidth() and colofframe==PicArray[i].GetColour():
        desc=PicArray[i].GetDescription() 
        width=PicArray[i].GetWidth()
        height=PicArray[i].GetHeight()
        print (desc + " " + str(width) + " " + str(height))





