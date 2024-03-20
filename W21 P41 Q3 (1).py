ArrayNodes=[[0 for col in range(3)] for row in range(20)]
RootPointer=-1
FreeNode=0

def AddNode(ArrayNodes,RootPointer,FreeNode):
    NodeData=input('Please enter the data to be inserted: ')
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            Placed=False
            CurrentNode=RootPointer
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
        print('Tree is full') 
    return ArrayNodes,RootPointer,FreeNode

def PrintAll(ArrayNodes):
    for CurrentPointer in range(20):
        print(f'{ArrayNodes[CurrentPointer][0]}   {ArrayNodes[CurrentPointer][1]}   {ArrayNodes[CurrentPointer][2]}')
        

for i in range(10):
    ArrayNodes,RootPointer,FreeNode=AddNode(ArrayNodes,RootPointer,FreeNode)        
PrintAll(ArrayNodes)

def InOrder(ArrayNodes,RootPointer,FreeNode):
    if RootPointer!=-1:
        InOrder(ArrayNodes,ArrayNodes[RootPointer][0],FreeNode)
        print(ArrayNodes[RootPointer][1])
        InOrder(ArrayNodes,ArrayNodes[RootPointer][2],FreeNode)

InOrder(ArrayNodes,RootPointer,FreeNode)





