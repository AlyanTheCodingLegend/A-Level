global DataArray
DataArray=[0 for i in range(100)]
#DECLARE DataArray:ARRAY[0:99] OF INTEGER

def ReadFile():
    try:
        global DataArray
        filehandle=open("IntegerData.txt","r")
        for i in range(100):
            DataArray[i]=int(filehandle.readline().strip())
        filehandle.close()    
    except IOError:
        print("File named IntegerData.txt was not found.")

def FindValues():
    global DataArray
    searchnum=0
    count=0
    while searchnum<1 or searchnum>100:
        searchnum=int(input("Please enter the number to be searched in the array: "))
    for i in range(100):
        if DataArray[i]==searchnum:
            count+=1    
    return count

ReadFile()
count=FindValues()
print("The value to be searched was found in the array "+str(count)+" times.")

def BubbleSort():
    global DataArray
    for i in range(100):
        for j in range(99):
            if DataArray[j]>DataArray[j+1]:
                temp=DataArray[j]
                DataArray[j]=DataArray[j+1]
                DataArray[j+1]=temp
    print(DataArray)            

BubbleSort()    