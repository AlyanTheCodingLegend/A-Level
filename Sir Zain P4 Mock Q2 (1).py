PollData=[-1 for i in range(10)] #PollData:Array [1:10] of Integer
CardData=[-1 for i in range(10)] #CardDara:Array [1:10] of Integer
PollData=[12,85,52,57,25,11,33,59,56,91]
CardData=[11,12,25,33,52,56,57,59,91,85]

def sortCardData():
    global CardData
    ArraySize=10
    for Pointer in range(2,ArraySize):
        ValueToInsert=CardData[Pointer]
        HolePosition=Pointer
        while HolePosition>1 and CardData[HolePosition-1]>ValueToInsert:
            CardData[HolePosition]=CardData[HolePosition-1]
            HolePosition=HolePosition-1
        CardData[HolePosition]=ValueToInsert    

def BinarySearch(CardData,SearchValue):
    First=1
    Last=len(CardData)
    Found=False
    while First<=Last and not(Found):
        Midpoint=int((First+Last)/2)
        if CardData[Midpoint]==SearchValue:
            Found=True
            print("The value has been found!")
        else:
            if SearchValue<CardData[Midpoint]:
                Last=Midpoint-1
            else:
                First=Midpoint+1
    if Found==False:
        print("The value has not been found!")

sortCardData()
searchval=int(input("Please enter the value to be searched: "))
BinarySearch(CardData,searchval)


