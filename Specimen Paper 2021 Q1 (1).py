TheData=[0 for i in range(9)] #TheData:ARRAY of Integer
TheData[0]=20
TheData[1]=3
TheData[2]=4
TheData[3]=8
TheData[4]=12
TheData[5]=99
TheData[6]=4
TheData[7]=26
TheData[8]=4

def InsertionSort(TheData):
    for Count in range(len(TheData)):
        DataToInsert=TheData[Count]
        Inserted=0
        NextValue=Count-1
        while (NextValue>=0 and Inserted!=1):
            if (DataToInsert<TheData[NextValue]):
                TheData[NextValue+1]=TheData[NextValue]
                NextValue=NextValue-1
                TheData[NextValue+1]=DataToInsert
            else:
                Inserted=1

def PrintArray(TheData):
    for i in range(9):
        print(TheData[i])

print("Data before sorting: ")
PrintArray(TheData)
InsertionSort(TheData)
print("Data after sorting: ")
PrintArray(TheData)

def FindData(TheData):
    found=False
    numtobefound=int(input("Please enter a whole number: "))
    for i in range(9):
        if (numtobefound==TheData[i]):
            found=True
    if found==True:
        print("found")
        return found
    else:
        print("not found")
        return found   


found=FindData(TheData)







