class node:
    def __init__(self,d,p):
        self.data=d # data is integer
        self.nextNode=p # nextNode is integer

linkedList=[]

# linkedList is an array of type node() with 10 elements

linkedList.append(node(1,1))
linkedList.append(node(5,4))
linkedList.append(node(6,7))
linkedList.append(node(7,-1))
linkedList.append(node(2,2))
linkedList.append(node(0,6))
linkedList.append(node(0,8))
linkedList.append(node(56,3))
linkedList.append(node(0,9))
linkedList.append(node(0,-1))

startPointer=0 # declare startPointer as an integer
emptyList=5 # declare emptyList as an integer

def outputNodes(list,start):
    currentptr=start
    while currentptr!=-1:
        print(f"Data: {list[currentptr].data}")
        currentptr=list[currentptr].nextNode

outputNodes(linkedList,startPointer)        

def addNode(list,start,free):
    item_to_be_added=int(input("Please enter the data to be added: "))
    if free<0 or free>9:
        return False,list,start,free
    else:
        list[free].data=item_to_be_added
        currentptr=start
        prevptr=-1
        while currentptr!=-1:
            prevptr=currentptr
            currentptr=list[currentptr].nextNode
        list[prevptr].nextNode=free
        temp=list[free].nextNode
        list[free].nextNode=-1
        free=temp

        return True,list,start,free

def addNodeTwo(list,start,free):
    item_to_be_added=int(input("Please enter the data to be added: "))
    if free<0 or free>9:
        return False,list,start,free
    else:
        list[free]=node(item_to_be_added,-1)
        currentptr=start
        prevptr=-1
        while currentptr!=-1:
            prevptr=currentptr
            currentptr=list[currentptr].nextNode
        list[prevptr].nextNode=free
        free=list[free].nextNode

        return True,list,start,free





outputNodes(linkedList,startPointer)   
flag,linkedList,startPointer,emptyList=addNodeTwo(linkedList,startPointer,emptyList)  
outputNodes(linkedList,startPointer)

if flag:
    print("Data has been added successfully.")
else:
    print("Linked List was full.") 


