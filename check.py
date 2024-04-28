class node:
    def __init__(self, dataP, nextNodeP):
        self.data = dataP  # INTEGER
        self.nextNode = nextNodeP  # INTEGER

# DECLARE linkedList:ARRAY[0:9] OF node        note that 0 and 9 are both inclusive in pseudocode
linkedList = [node(1, 1), node(5, 2), node(6, 3), node(7, 4),
              node(21, 5), node(0, 6), node(0, 7), node(0, 8),
              node(0, 9), node(0, -1)]

startPointer = 0  # this will always point to the first element and not change
emptyList = 5

def outputNodes():
    global linkedList, startPointer
    currentPointer = startPointer

    while currentPointer != -1:  # Corrected loop condition
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode

outputNodes()

def orderedInsertion():
    global linkedList, emptyList, startPointer

    dataToInsert = int(input("enter the data to be inserted: "))

    if emptyList < 0 or emptyList > 9:
        return False
    else:
        freeList = emptyList
        emptyList = linkedList[emptyList].nextNode

        newNode = node(dataToInsert, -1)

        linkedList[freeList] = newNode

        previousPointer = None
        currentPointer = startPointer

        while currentPointer != -1 and linkedList[currentPointer].data < dataToInsert:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode

        if previousPointer is None:
            linkedList[freeList].nextNode = startPointer
            startPointer = freeList
        else:
            linkedList[freeList].nextNode = linkedList[previousPointer].nextNode
            linkedList[previousPointer].nextNode = freeList

        return True

val = orderedInsertion()
print(val)
outputNodes()
