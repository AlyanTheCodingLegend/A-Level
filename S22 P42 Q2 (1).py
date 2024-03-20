from random import randint
global RandArray
RandArray=[[0 for i in range(10)] for j in range(10)] #DECLARE RandArray:ARRAY[0:9,0:9] OF INTEGER
for i in range(10):
    for j in range(10):
        RandArray[i][j]=randint(1,100)

def OutArray():
    for i in range(10):
        for j in range(10):
            print(RandArray[i][j]," ",end='')
        print("")


print("BEFORE: ")
OutArray()


ArrayLength=10
for x in range(ArrayLength):
    for y in range(ArrayLength-1):
        for z in range(ArrayLength-y-1):
            if RandArray[x][z]>RandArray[x][z+1]:
                TempValue=RandArray[x][z]
                RandArray[x][z]=RandArray[x][z+1]
                RandArray[x][z+1]=TempValue


print("AFTER: ")
OutArray()

def BinarySearch(RandArray,lower,upper,searchval):
    upper=int(upper)
    lower=int(lower)
    searchval=int(searchval)
    if upper>lower:
        mid=int(((lower)+(upper-1))/2)
        if RandArray[0][mid]==searchval:
            return mid
        else:
            if RandArray[0][mid]>searchval:
                return BinarySearch(RandArray,lower,mid-1,searchval)
            else:
                return BinarySearch(RandArray,mid+1,upper,searchval)
    return -1

for i in range(2):
    searchval=int(input("Please enter the value to be searched: "))
    returnval=BinarySearch(RandArray,0,9,searchval)
    print(returnval)