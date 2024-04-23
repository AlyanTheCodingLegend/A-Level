# DECLARE ArrayNodes....
ArrayNodes=[[-1 for _ in range(3)] for _ in range(20)]

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

def SearchValue(Root, ValueToFind):
    global ArrayNodes

    if Root==-1: # list is searched but value is not found yet
        return -1
    else:
        if ArrayNodes[Root][1]==ValueToFind: # data is found
            return Root
        else:
            if ArrayNodes[Root][1]==-1: # free node
                return -1

    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    
# Pre-Order Traversal
# output the root
# visit the left
# visit the right

# In-Order Traversal
# visit the left
# output the root
# visit the right

# Post-Order Traversal
# visit the left
# visit the right
# output the root

def PostOrder(Root):
    global ArrayNodes

    if ArrayNodes[Root][0]!=-1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2]!=-1:
        PostOrder(ArrayNodes[Root][2])
    print(f"Left: {ArrayNodes[Root][0]} Data: {ArrayNodes[Root][1]} Right: {ArrayNodes[Root][2]}")    

result=SearchValue(RootPointer,15)
if result==-1:
    print("Result was not found")
else:
    print(f"Value found at index: {result}")

PostOrder(RootPointer)

# Add node function which will be recursive

# base case: there is no space, free
# general case: we will just call the function with left/right pointer as parameter

def AddNode(Root,ValueToAdd):
    global ArrayNodes, FreeNode

    if FreeNode>19: # Array is full
        return Root,-1

    ArrayNodes[FreeNode][1]=ValueToAdd # data has been inserted

    if Root==-1: # Array is empty
        Root=FreeNode
        FreeNode+=1
        return Root,1

    if ArrayNodes[Root][1]>ValueToAdd:
        if ArrayNodes[Root][0]!=-1: # iterating
            AddNode(ArrayNodes[Root][0], ValueToAdd)
        else: # finalizing the insertion
            ArrayNodes[Root][0]=FreeNode # updating left pointer to connect the current node
            FreeNode+=1
            return Root,1 # stops recursion

    if ArrayNodes[Root][1]<ValueToAdd:
        if ArrayNodes[Root][2]!=-1: # iterating
            AddNode(ArrayNodes[Root][2], ValueToAdd)
        else: # finalizing the insertion
            ArrayNodes[Root][2]=FreeNode # updating right pointer to connect the current node
            FreeNode+=1
            return Root,1 # stops recursion
    
RootPointer,resultTwo=AddNode(RootPointer,7)
if resultTwo==-1:
    print("Array was full")
else:
    print("Data added successfully!")

PostOrder(RootPointer)    

print(ArrayNodes)