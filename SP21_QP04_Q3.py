QueueData=["" for i in range(20)]
Head=0
Tail=0

def Enqueue(item):
    global Tail
    global QueueData
    global Head
    if Tail==20:
        return False
    else:
        QueueData[Tail]=item
        Tail+=1
        return True
    
def ReadFile():
    global QueueData
    global Tail
    global Head
    filename=input("Please enter a file name: ")
    try:
        file=open(filename,"r")
        line=file.readline().strip()
        flag=True
        while flag and line:
            flag=Enqueue(line)
            line=file.readline().strip()
        if flag==False: # Queue is full
            file.close()
            return 1
        else: # text file is completely read and stored
            file.close()
            return 2
    except FileNotFoundError:
        return -1 # file is non-existent
    
output=ReadFile()
if output==-1:
    print("File did not exist.")
elif output==1:
    print("Queue was full.")
elif output==2:
    print("All items were added to the queue.")

def Remove():
    global QueueData
    global Head
    global Tail
    if Tail<2:
        return "No Items"
    else:
        str1=QueueData[Head]
        Head+=1
        str2=QueueData[Head]
        Head+=1
        returnstr=str1+" "+str2
        return returnstr

print(Remove())