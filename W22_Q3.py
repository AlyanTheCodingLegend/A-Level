'''
ArrayNodes=[[-1 for col in range(3)] for row in range(20)]

FreeNode=6
RootPointer=0

ArrayNodes[0][0]=1
ArrayNodes[0][1]=20
ArrayNodes[0][2]=5
ArrayNodes[1][0]=2
ArrayNodes[1][1]=15
ArrayNodes[2][1]=3
ArrayNodes[2][2]=3
ArrayNodes[3][1]=9
ArrayNodes[3][2]=4
ArrayNodes[4][1]=10
ArrayNodes[5][1]=58

def SearchValue(Root,ValueToFind):
    global ArrayNodes
    global FreeNode

    if Root==-1: # starting condition
        return -1
    else:
        if ArrayNodes[Root][1]==ValueToFind: 
            return Root
        else:
            if ArrayNodes[Root][1]==-1: # base case
                return -1
    
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0],ValueToFind) # general case

    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind) # general case

def PostOrder(Root):
    global ArrayNodes
    global FreeNode

    if ArrayNodes[Root][0]!=-1: # left not empty
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2]!=-1: # right not empty    
        PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])    

found=SearchValue(RootPointer,15)

if found==-1:
    print("Value was not found")
else:
    print(f"Value found at index: {found}")

PostOrder(RootPointer)        

'''
ArrayNodes=[[-1 for col in range(3)] for row in range(20)]
RootPointer=-1
FreeNode=0

def AddNode():
    global ArrayNodes # by reference
    global RootPointer
    global FreeNode

    NodeData=int(input("Enter the data: "))
    if FreeNode <=19: # list is not full
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1: # tree is empty, data to be added to root
            RootPointer=0
        else:
            Placed=False # flag
            CurrentNode=RootPointer # main pointer used to traverse
            while Placed==False:
                if NodeData<ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2]==-1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][2]
        FreeNode=FreeNode+1
    else:
        print("Tree is full")                


def PrintAll():
    global ArrayNodes
    print("L\tD\tR")
    for i in range(FreeNode):
        print(f"{ArrayNodes[i][0]}\t{ArrayNodes[i][1]}\t{ArrayNodes[i][2]}")

'''
def PrintAll(ArrayNodes): 
    for X in range(0, 20): 
        print(str(ArrayNodes[X][0]), " ", str(ArrayNodes[X][1]), " ", str(ArrayNodes[X][2])) 
'''
for i in range(10):
    AddNode()

PrintAll()

def InOrder(RootPointer):
    global ArrayNodes 
    global FreeNode

    print(ArrayNodes[RootPointer][1])   
    if ArrayNodes[RootPointer][0]!=-1:
        InOrder(ArrayNodes[RootPointer][0])  
    print(ArrayNodes[RootPointer][1])     
    if ArrayNodes[RootPointer][2]!=-1:
        InOrder(ArrayNodes[RootPointer][2])   



print("\n")
InOrder(RootPointer)