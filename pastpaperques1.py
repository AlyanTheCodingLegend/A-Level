class Card:
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP  # Integer
        self.__Colour = ColourP  # String

    
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


array = [Card(0, "") for _ in range(30)]

try:
    file = open("CardValues.txt", "r")

    for i in range(30):

        number=int(file.readline())
        colour=file.readline()

        array[i]=Card(number,colour)

    file.close()    
except FileNotFoundError:
    print("File not found!")
    

selectedCards=[]

def ChooseCard():
    global selectedCards

    while True:
        cardnum=int(input("Enter index between 1 and 30: "))
        while cardnum<1 or cardnum>30:
            print("Invalid index!")
            cardnum=int(input("Enter index between 1 and 30: "))
        
        if cardnum in selectedCards:
            print("Card already selected!")
        else:
            print("Valid")
            break    

    selectedCards.append(cardnum) # marks it as selected       
    
    return cardnum # returns index of cardnum


Player1 = [Card(0,"") for _ in range(4)]
for i in range(4):
    selectedCardIndex = ChooseCard()

    Player1[i]=array[selectedCardIndex-1]

    print(f"Number: {Player1[i].GetNumber()} Colour: {Player1[i].GetColour()}")


    
