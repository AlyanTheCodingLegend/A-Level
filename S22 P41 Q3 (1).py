global QueueArray,headpointer,tailpointer,noofitems
QueueArray=["" for i in range(10)] #DECLARE QueueArray:ARRAY[0:9] OF STRING
headpointer=0 #INTEGER
tailpointer=0 #INTEGER
noofitems=0 #INTEGER

def Enqueue(QueueArray,headpointer,tailpointer,noofitems,datatoadd):
    if int(noofitems)==10:
        return False,QueueArray,headpointer,tailpointer,noofitems
    QueueArray[tailpointer]=datatoadd
    if int(tailpointer)>=9:
        tailpointer=0
    else:
        tailpointer=tailpointer+1
    noofitems=noofitems+1
    return True,QueueArray,headpointer,tailpointer,noofitems
        
def Dequeue(QueueArray,headpointer,tailpointer,noofitems):
    if int(noofitems)==0:
        return False,QueueArray,headpointer,tailpointer,noofitems
    datatoremove=QueueArray[headpointer]
    if int(headpointer)>=9:
        headpointer=0
    else:
        headpointer=headpointer+1    
    noofitems=noofitems-1
    return datatoremove,QueueArray,headpointer,tailpointer,noofitems
        
for i in range(11):
    datatoadd=input("Please enter the data to be added to the queue: ")
    flag,QueueArray,headpointer,tailpointer,noofitems=Enqueue(QueueArray,headpointer,tailpointer,noofitems,datatoadd)
    if flag==True:
        print("Data was added successfully.")
    else:
        print("Data was not added as queue is full.")

print(QueueArray)

for j in range(2):
    returnval,QueueArray,headpointer,tailpointer,noofitems=Dequeue(QueueArray,headpointer,tailpointer,noofitems)
    print(returnval)

print(QueueArray)    