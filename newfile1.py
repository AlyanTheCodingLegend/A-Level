class node:
    def __init__(self,data,nextNode):
        self.data=data # data as Integer
        self.nextNode=nextNode # nextNode as Integer

# startPointer as Integer
# emptyList as Integer

startPointer=0
emptyList=5

# DECLARE linkedList: ARRAY[0:9] OF node

linkedList=[]

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

def outputNodes(linkedList,startPointer):

    currentPointer=startPointer

    while currentPointer!=-1:
        print(f"Data: {linkedList[currentPointer].data}")

        currentPointer=linkedList[currentPointer].nextNode

# outputNodes(linkedList,startPointer)








def addNode(linkedList, startPointer, emptyList):

    datatobeadded=int(input("Please enter the data to be added: "))

    if emptyList<0 or emptyList>9:
        return False
    
    # this code running means that space is empty

    linkedList[emptyList].data=datatobeadded

    prevPointer=-1
    currentPointer=startPointer 

    while currentPointer!=-1:
        prevPointer=currentPointer # 3
        currentPointer=linkedList[currentPointer].nextNode # -1

    linkedList[prevPointer].nextNode=emptyList
    emptylist=linkedList[emptyList].nextNode # idhar

    return True

outputNodes(linkedList,startPointer)

result=addNode(linkedList,startPointer,emptyList)

if result==True:
    print("Data was added successfully!")
else:
    print("List is full!")

outputNodes(linkedList,startPointer)



    






    






    