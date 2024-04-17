class Picture:
    def __init__(self, descriptionP, widthP, heightP, colourP):
        self.__Description = descriptionP  # STRING
        self.__Width = widthP  # INTEGER
        self.__Height = heightP  # INTEGER
        self.__FrameColour = colourP  # STRING

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetColour(self):
        return self.__FrameColour


    def SetDescription(self, newDescription):
        self.__Description = newDescription

PictureArray = [Picture("",0,0,"") for _ in range(100)]
# DECLARE PictureArray:ARRAY[0:99] OF Picture

def ReadData():
    global PictureArray  # passing array by reference or global array declared
    count = 0
    try:
        file = open("Pictures.txt", "r")
        datafetched = file.readline().strip().lower()
        while datafetched != "":
            description = datafetched
            width = int(file.readline().strip())
            height = int(file.readline().strip())  # text file will has it in string format
            colour = file.readline().strip().lower()
            PictureArray[count]=Picture(description, width, height, colour)
            count += 1
            datafetched = file.readline().strip().lower()

        file.close()
        return count  # return means that you will exit the function so it must be after file.close() so that the file can be closed

    except IOError:
        print("file not found")


PictureCount = ReadData()
print(PictureCount)

colour = input("enter the colour of the frame:").lower()  # instead of - colour = colour.lower(), just put lower in the same line
width = int(input("enter the maximum width of the picture:"))
height = int(input("enter the maximum height of the picture:"))

for i in range(PictureCount):
    if PictureArray[i].GetColour() == colour:
        if PictureArray[i].GetWidth() <= width:
            if PictureArray[i].GetHeight() <= height:
                print(PictureArray[i].GetDescription(), PictureArray[i].GetHeight(), PictureArray[i].GetWidth())

# [""] array length=1, string=0
# [] array length=0
# "" is an object of class String
# 0 is an object of class Integer
# 0.0 is an object of class float
# false/true is an object of class boolean




