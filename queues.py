# 2 implementations: linear, circular

# a linear queue can get full, u cant enter more data

# a circular queue updates the data

class SaleData:
    def __init__(self,idP, quantityP):
        self.id=idP # id as String
        self.quantity=quantityP # quantity as Integer

CircularQueue = [SaleData("", -1) for i in range(5)]  # DECLARE CircularQueue: ARRAY[0:4] OF SaleData
Head = 0 # DECLARE Head: INTEGER
Tail = 0 # DECLARE Tail:INTEGER
NumberOfItems = 0  # DECLARE NumberOfItems: INTEGER

def Enqueue(additem):
    global CircularQueue, Head, Tail, NumberOfItems

    if NumberOfItems==5:
        return -1
    
    CircularQueue[Tail].id=additem.id
    CircularQueue[Tail].quantity=additem.quantity

    # FIFO (first in, first out)

    # insertion happens through Tail, removing happens through Head 

    Tail+=1 # Tail=4, Tail=5->0
    NumberOfItems+=1

    if Tail>4:
        Tail=0 # in linear queue, u would simply output "Queue is full"

    return 1

def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems

    if NumberOfItems == 0:
        return SaleData("", -1)
    
    record=CircularQueue[Head]
    Head+=1
    NumberOfItems -= 1
    
    # pointers updating
    if Head>4: # in linear queue, you would simply output "Queue is empty"
        Head = 0

    return record   # anything after the return statement is not run


def EnterRecord():
    id = input("enter the id: ")
    quantity = int(input("enter the quantity: "))
    stored = Enqueue(SaleData(id, quantity))
    if stored == 1:
        print("Stored")
    else:
        print("Full")


for i in range(6):
    EnterRecord()

removedRecord = Dequeue()

if removedRecord.id=="" and removedRecord.quantity==-1:  # cannot compare object
 
 
 
 
    print("Circular Queue is empty!")
else:
    print(f"ID: {removedRecord.id} | Quantity: {removedRecord.quantity}")

EnterRecord()

for j in range(len(CircularQueue)):
    print(f"ID: {CircularQueue[j].id} | Quantity: {CircularQueue[j].quantity}")