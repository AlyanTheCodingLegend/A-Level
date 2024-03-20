global StackData
global StackPointer
StackData=[0 for i in range(10)] #DECLARE StackData:ARRAY[0:9] OF INTEGER
StackPointer=0 #INTEGER

def OutputVal():
    for i in range(10):
        print (StackData[i])
    print (StackPointer)

def Push(valtoadd,StackPointer):
    if StackPointer>9:
        return False,StackPointer
    else:
        StackData[StackPointer]=valtoadd
        StackPointer+=1
        return True,StackPointer

for i in range(11):
    valtoadd=int(input("Please enter the value to be added to the stack: "))
    flag,StackPointer=Push(valtoadd,StackPointer)
    if flag==True:
        print("Value has successfully been added to the stack.")
    else:
        print("Value can not be added to the stack as the stack is full.")

print(StackData)
print(StackPointer)                    

def Pop(StackPointer):
    if StackPointer==0:
        return -1,StackPointer
    else:
        valtoremove=StackData[StackPointer-1]
        StackPointer-=1
        return valtoremove,StackPointer
    
for i in range(2):
    val,StackPointer=Pop(StackPointer) 

print(StackData)
print(StackPointer)       