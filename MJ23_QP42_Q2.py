class SaleData:
    def __init__(self,id,q):
        self.id=id 
        self.quantity=q

CircularQueue=[SaleData("",-1) for i in range(5)]
Head=0
Tail=0
NumberofItems=0

def Enqueue(salerec):
    global NumberofItems
    global CircularQueue
    global Head
    global Tail
    if (NumberofItems==5):
        return -1
    else:
        CircularQueue[Tail]=salerec
        if Tail==4:
            Tail=0
        else:
            Tail+=1
        NumberofItems+=1
        return 1        

def Dequeue():
    global NumberofItems
    global CircularQueue
    global Head
    global Tail
    record_removed=SaleData("",-1)
    if NumberofItems!=0:
        record_removed=CircularQueue[Head]
        NumberofItems-=1
        if Head==4:
            Head=0 
        else:
            Head+=1
    return record_removed            

def EnterRecord():
    sid=input("Please enter a sale ID: ")
    squantity=int(input("Please enter a quantity: "))
    salerecord=SaleData(sid,squantity)
    if Enqueue(salerecord)==1:
        print("Stored")
    elif Enqueue(salerecord)==-1:
        print("Full")

for i in range(6):
    EnterRecord()

salerec=Dequeue()

if salerec.id=="":
    print("Queue was empty, record could not be removed.")
else:
    print(f"Sale ID: {salerec.id} Sale Quantity: {salerec.quantity}")

EnterRecord() # enter LLP record again

for i in range(len(CircularQueue)):
    print(f"Sale ID: {CircularQueue[i].id} Sale Quantity: {CircularQueue[i].quantity}")





    