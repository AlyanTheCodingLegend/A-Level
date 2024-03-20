# 1: nodes-> class list-> array
# 2: nodes and list -> 2d array
# 3: nodes aur list -> classes

class node:
    def __init__(self,data,pointer):
        self.data=data
        self.pointer=pointer

linkedList=[node("",-1) for i in range(10)]
headP=-1 # stores index of first filled node
freeP=0 # stores index of first free node

# array[2] array=[4,6,1,2,8,9]

def addNode(dataValue):
    global linkedList
    global headP
    global freeP

    if freeP==-1: # linked list is completely full
        return "Data can not be stored as list is full"
    else:
        if headP==-1: # linked list is completely empty
            linkedList[freeP].data=dataValue
            headP=freeP
            # headP is now 0, freeP is also 0
            freeP=linkedList[freeP].pointer
        elif freeP==9: # linked list only has last node free
            linkedList[freeP].data=dataValue

        else: # linked list has some places free
            pass






