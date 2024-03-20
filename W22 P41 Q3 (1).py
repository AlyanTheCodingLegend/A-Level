global ArrayNodes
ArrayNodes=[[0 for i in range(3)] for j in range(20)]
for i in range(3):
    for j in range(20):
        ArrayNodes[j][i]=-1
     
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
FreeNode=6
RootPointer=0

def SearchValue(Root,ValueToFind):
    global ArrayNodes
    ValueToFind=int(ValueToFind)
    if Root==-1:
        return -1
    else:
        if ArrayNodes[Root][1]==ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1]==-1:
                return -1
    if ArrayNodes[Root][1]>ValueToFind:
        return SearchValue(ArrayNodes[Root][0],ValueToFind)
    if ArrayNodes[Root][1]<ValueToFind:
        return SearchValue(ArrayNodes[Root][2],ValueToFind)       

def PostOrder(Root):
    global ArrayNodes
    if ArrayNodes[Root][0]!=-1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2]!=-1:
        PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])

val=SearchValue(RootPointer,15)
if val==-1:
    print("The value was not found in the binary tree.")            
else:
    print("The value was found at index: "+str(val))
PostOrder(RootPointer)

