Queue=[int for i in range(100)]
headPointer=-1
tailPointer=0

def Enqueue(integer_val):
    global Queue
    global head
    global tail
    if tail>99 or tail<0: 
        return False
    if head==-1: 
        head=tail
    Queue[tail]=integer_val
    tailPointer=tailPointer+1
    return True


stored=True
for i in range(1,21):
    stored=Enqueue(i)
    if stored==False:
        break

if stored:
    print("Successful")
else:
    print("Unsuccessful")

def RecursiveOutput(start):
    global Queue
    global head
    global tail
    if start==head:
        return 0
    else:
        return Queue[start-1]+RecursiveOutput(start-1)

print(f"The sum of all values in the queue is: {RecursiveOutput(tailPointer)}")
