# 3 impementations: 
# 1. record aur array: class Node, linked list-> array
# 2. 2d arrays
# 3. full record

class Node:
    def __init__(self, data, pointer):
        self.data=data
        self.pointer=pointer

linkedList=[Node("",-1) for i in range(10)] # this array has 10 nodes, meaning list has 10 nodes

linkedList=[["" for col in range(2)] for row in range(10)]

# row represents a Node
# 1st column represents data, 2nd column represents pointer

# now, we will connect the nodes to construct the linked list

# Node 0: p: 1
# node 1 p: 2
# .....
# node 8 p:9
# node 9 p:10

for i in range(9):
    (linkedList[i]).pointer=i+1

headP=-1 # point to the first EVER filled node
freeP=0 # points to the first empty node
    
# linked list is created and linked
    
# search, adding, delete
    
# head: 8th index p: 4
# 4th index p: 9
# 9th index p: 6
# ...........

def searchNode(dataitem):
    global linkedList
    global headP
    global freeP

    currentP=headP # helps us loop/ iterate through this whole list
    found=False # tells if data item is found or not 

    while currentP!=freeP: # we will not search the empty nodes
        if (linkedList[currentP]).data==dataitem:
            found=True
            break
        else:
            currentP=(linkedList[currentP]).pointer

    if found==True:
        print(f"Data item found at {currentP}")
    else:
        print("Data item not found")

# we are taking a data item as input, we are adding it to the linked list at the first empty space
# we updated the pointers accordingly to handle edge cases (list is full or empty)
        
def addNode(datatobeadded):
    global linkedList
    global headP
    global freeP 

    if freeP==-1: # list is full
        return "List is full"

    linkedList[freeP].data=datatobeadded # insert data at insertion point

    if headP==-1: # list is empty
        headP=freeP # updated headP
    
    freeP=linkedList[freeP].pointer

    return "Data value added"

def deleteNode(datatobedeleted):
    global linkedList
    global headP
    global freeP

    prevP=-1
    currentP=headP
    nextP=linkedList[headP].pointer
    found=False

    if headP==-1: # lis is actually empty
        return "List is empty"

    while currentP!=freeP:

        if datatobedeleted==linkedList[currentP].data: # if data to be deleted is found
            
            linkedList[currentP].data="" # to signify that there is no data here

            if currentP==headP: # headP needs to be removed
                headP=(linkedList[currentP]).pointer # updating the headP
                linkedList[currentP].pointer=-1

            elif nextP==-1:
                linkedList[currentP].pointer=-1
                linkedList[prevP].pointer=-1

            else: # data to be deleted was found somehwere in the middle

                linkedList[prevP].pointer=nextP
                linkedList[currentP].pointer=-1

            found=True

        else: # increment all ptrs
            prevP=currentP 
            currentP=nextP
            nextP=linkedList[nextP].pointer

    if found==True:
        print("Data is deleted")
    else:
        print("data was not found")

def insertAfter(item, after):
    global linkedList, headP, freeP

    if freeP==-1:
        print("Linked list is full.")
    else:
        if headP==-1:
            print("List is empty.")
        else:
            newNodeP=freeP
            currentPointer=headP
            search=True

            while search:
                currentData=linkedList[currentPointer].data

                if currentData==after:
                    search=False
                else:
                    currentPointer=linkedList[currentPointer].pointer
                    if currentPointer==-1:
                        search=False

            if currentPointer==-1:
                print(f"The node with data {after} was not found.")
            else:
                freeP=linkedList[freeP].pointer # freeP increments to new available space
                linkedList[newNodeP].data=item # data is stored in the node
                nextNodeP=linkedList[currentPointer].pointer # storing index of nextNode in a temporary variable FROM the previous node's pointer
                linkedList[currentPointer].pointer=newNodeP # connecting previous node with NEW node by over writing previous node pointer's value
                linkedList[newNodeP].pointer=nextNodeP # connecting NEW node to the next node using new node's pointer
                print("Item added.")











    
