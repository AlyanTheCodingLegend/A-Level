# 5 days per week
# 3 days 

# halving ur days, double ur topics covered

# notes topic1, topic 2(parhai karna) -> topicals topic 1 and 2

# DECLARE TheData: ARRAY[0:8] OF INTEGER
TheData = [20,3,4,8,12,99,4,26,4]

def InsertionSort():

    global TheData

    for Count in range(0,len(TheData)): # for loop is responsible for passes
        DataToInsert=TheData[Count]
        Inserted=0
        NextValue=Count-1

        while (NextValue>=0 and Inserted!=1): # while loop does swapping
            if (DataToInsert<TheData[NextValue]): # swapping will take place
                TheData[NextValue+1]=TheData[NextValue]
                NextValue-=1
                TheData[NextValue+1]=DataToInsert
            else: # no need for swapping because data is already sorted TILL this point
                Inserted=1
           

# [20, 3, 4, 8, 12, 99, 4, 26, 4]

# i=0, element=20 (ignore for now)

def outputContents(TheData):
    for i in range(len(TheData)):
        print(TheData[i])

print("Before sorting:\n")
outputContents(TheData)
InsertionSort()
print("\nAfter sorting:\n")
outputContents(TheData)

def LinearSearch():

    global TheData

    data=int(input("Enter a whole number to be searched: "))

    for i in range(len(TheData)):
        if data==TheData[i]:
            print("found")
            return True

    print("not found")        
    return False

LinearSearch() # input 8 to test
LinearSearch() # input 9 to test
