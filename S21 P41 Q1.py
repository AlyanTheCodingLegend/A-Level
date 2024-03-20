class node:
    def __init__(self):
        self.data=0
        self.nextNode=-1

linkedList=[node() for i in range(0,10)]
linkedList[0].data=1
linkedList[0].nextNode=1
linkedList[1].data=5
linkedList[1].nextNode=4
linkedList[2].data=6
linkedList[2].nextNode=7
linkedList[3].data=7
linkedList[4].data=2
linkedList[4].nextNode=2
linkedList[5].nextNode=6
linkedList[6].nextNode=8
linkedList[7].data=56
linkedList[7].nextNode=3
linkedList[8].nextNode=9
startPointer=0
emptyList=5

def outputNodes(linkedList,startPointer):
    currentpointer=startPointer
    while currentpointer!=-1:
        print(linkedList[currentpointer].data)
        currentpointer=linkedList[currentpointer].nextNode

outputNodes(linkedList,startPointer)
print()

def addNode(linkedList,startPointer,emptyList):
    inputdata=input('Please enter the data to be inputted.')
    currentpointer=startPointer
    if emptyList==-1:
        return False,linkedList,startPointer,emptyList
    elif startPointer==-1:
        linkedList[emptyList].data=inputdata
        linkedList[emptyList].nextNode=-1
        startPointer=emptyList
        while currentpointer!=-1:
            prevNodeP=currentpointer
            currentpointer=linkedList[currentpointer].nextNode
        linkedList[prevNodeP].nextNode=emptyList 
        emptyList=linkedList[emptyList].nextNode
        return True,linkedList,startPointer,emptyList
    else:
        linkedList[emptyList].data=inputdata
        linkedList[emptyList].nextNode=-1
        while currentpointer!=-1:
            prevNodeP=currentpointer
            currentpointer=linkedList[currentpointer].nextNode
        linkedList[prevNodeP].nextNode=emptyList    
        emptyList=linkedList[emptyList].nextNode
        return True,linkedList,startPointer,emptyList

outputNodes(linkedList,startPointer)
dataadded,linkedList,startPointer,emptyList=addNode(linkedList,startPointer,emptyList)
if dataadded==True:
    print('Data is added.')
else:
    print('Data is not added as linked list was full.')    
outputNodes(linkedList,startPointer)



