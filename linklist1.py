class node:
    def __init__(self):
        self.data=-1
        self.pointer=-1

linkedList=[node() for _ in range(10)]        

for i in range(9):
    linkedList[i].pointer=i+1

linkedList[9].pointer=-1

startpointer=-1
freepointer=0

def add_data(item):
    global linkedList
    global startpointer
    global freepointer
    if freepointer==-1:
        print("List is full")
        return -1
    else:
        linkedList[freepointer]=item
        freepointer+=1
        if freepointer>9:
            freepointer=-1


itemnode=node()
def add_data2(itemnode):
    global linkedList
    global startpointer
    global freepointer

    
