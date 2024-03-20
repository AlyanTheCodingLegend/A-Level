# part a
# DECLARE arrayData[0:9] OF INTEGER
global arrayData
arrayData=[0 for i in range(10)]
arrayData=[10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# part b i/ii
item=int(input("Please enter the number to be searched."))
def linearSearch(item):
    flag=False
    for i in range(10):
        if arrayData[i]==item:
            flag=True
    if flag==True:
        print("The value has been found in the array.")   
    else:
        print("The value has not been found in the array.")     

linearSearch(item)            

# part c
def bubbleSort():
    temp=0
    for x in range(10):
        for y in range(9):
            if arrayData[y]<arrayData[y+1]:
                temp=arrayData[y]
                arrayData[y]=arrayData[y+1]
                arrayData[y+1]=temp
bubbleSort()
print(arrayData)                
