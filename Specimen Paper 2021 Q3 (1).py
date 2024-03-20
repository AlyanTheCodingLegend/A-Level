QueueData=["" for i in range(20)] #QueueData:ARRAY of String
StartPointer=-1 #StartPointer as Integer
EndPointer=-1 #EndPointer as Integer

def Enqueue(itemtobeadded):
    global QueueData,StartPointer,EndPointer
    if StartPointer==-1:
        QueueData[EndPointer+1]=itemtobeadded
        EndPointer=EndPointer+1
        StartPointer=StartPointer+1
        return True
    elif EndPointer<19:
        QueueData[EndPointer+1]=itemtobeadded
        EndPointer=EndPointer+1
        return True
    else:
        return False

def ReadFile():
    global QueueData,StartPointer,EndPointer
    try: 
        filename=input("Please enter the filename: ")
        filehandle=open(filename,"r")
        temp=filehandle.readline()
        for i in range(20):
            QueueData[i]=temp
            temp=filehandle.readline()
        if len(temp)!=0:
            return 2
        else:
            return 1    
    except IOError:
        return -1

output=ReadFile()
if output==1:
    print("All items were added to the queue.")
elif output==2:
    print("The queue was full so all of the data could not be added.")
elif output==-1:
    print("The text file could not be found.")  

def Remove():
    global QueueData,StartPointer,EndPointer
    if EndPointer>0:
        item1=QueueData[StartPointer]
        StartPointer=StartPointer+1
        item2=QueueData[StartPointer]
        StartPointer=StartPointer+1
        outstr=item1 + " " + item2
    else:
        outstr="No Items"
    return outstr
        





