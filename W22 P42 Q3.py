Queue=[] #Queue global array of Integer, 100 by 1 elements
headpointer=-1 # headpointer global integer 
tailpointer=0 #tailpointer global integer

def Enqueue(valuetobestored):
    global Queue
    global headpointer
    global tailpointer
    if tailpointer==0:
        headpointer=0
        Queue[tailpointer]=valuetobestored
        tailpointer+=1
        return True
    elif tailpointer>99:
        return False
    else:
        Queue[tailpointer]=valuetobestored
        tailpointer+=1
        return True

stored=True
i=0
while stored==True and i<21:
    stored=Enqueue(i)
    i+=1 
if stored==True:
    print("Successful")
else:
    print("Unsuccessful") 

def RecursiveOutput(Start):
    pass





total=RecursiveOutput()
print(f"The total value outputted is: {total}")




    