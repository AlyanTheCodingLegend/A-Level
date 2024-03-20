# Linked List Program.

# Creating a linked list of 10 elements which stores data items of type string, using object-oriented Programming(OOP).
# It is assumed that the linked list has an ascending order.
# If an element is empty assign "null" to it.

# Creating a node record:
class node:

    def __init__(self, dataP, pointerP):
        self.NodeData = dataP
        self.NodePointer = pointerP

# Creating an array/list object 'LinkedList' of type node:
LinkedList = [node for i in range(10)]
StartPointer = -1
FreePointer = 0

# Writing a procedure to initialize linked list of 10 nodes:
def InitializeList(LinkedList):
    for j in range(9):
        LinkedList[j] = node("null", j+1)    # "null" represents that the elements are empty 
    LinkedList[9] = node("null", -1)
    return LinkedList

LinkedList = InitializeList(LinkedList)

# Writing a procedure to output the values and pointers of the linked list:
def OutputList(LinkedList, FreePointer):
    for y in range(10):
        print(f"{LinkedList[y].NodeData}  {LinkedList[y].NodePointer}")
    print(f"Start Pointer: {StartPointer}")
    print(f"Free Pointer: {FreePointer}")

OutputList(LinkedList, FreePointer)
print()

# Writing a procedure to insert a new node in ordered linked list:
def InsertNode(DataItem, LinkedList, StartPointer, FreePointer):

    if FreePointer != -1:
        LinkedList[FreePointer].NodeData = DataItem
        TempFreePointer = LinkedList[FreePointer].NodePointer
        CurrentPointer = StartPointer

        while (DataItem > LinkedList[CurrentPointer].NodeData) and (CurrentPointer != -1):
            PreviousPointer = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer].NodePointer
        
        if CurrentPointer == StartPointer:
            LinkedList[FreePointer].NodePointer = StartPointer
            StartPointer = FreePointer

        else:
            LinkedList[FreePointer].NodePointer = LinkedList[PreviousPointer].NodePointer
            LinkedList[PreviousPointer].NodePointer = FreePointer

        FreePointer = TempFreePointer

    else:
        print("List is full!")

    return LinkedList, StartPointer, FreePointer


# Inserting some sample data items in the linked list and testing InsertNode():
InputValue = "T"
LinkedList, StartPointer, FreePointer = InsertNode(InputValue, LinkedList, StartPointer, FreePointer)
# OutputList(LinkedList, FreePointer)
InputValue = "Z"
LinkedList, StartPointer, FreePointer = InsertNode(InputValue, LinkedList, StartPointer, FreePointer)
# OutputList(LinkedList, FreePointer)
InputValue = "R"
LinkedList, StartPointer, FreePointer = InsertNode(InputValue, LinkedList, StartPointer, FreePointer)
# OutputList(LinkedList, FreePointer)
InputValue = "P"
LinkedList, StartPointer, FreePointer = InsertNode(InputValue, LinkedList, StartPointer, FreePointer)
# OutputList(LinkedList, FreePointer)
InputValue = "C"
LinkedList, StartPointer, FreePointer = InsertNode(InputValue, LinkedList, StartPointer, FreePointer)
OutputList(LinkedList, FreePointer)
print()


# Writing a procedure to search for an element in the linked list:
# Method 1 - Using linear search:
def SearchNode1(SearchItem, LinkedList, FreePointer):

    for i in range(FreePointer):
        if SearchItem == LinkedList[i].NodeData:
            return True, i
    return False, -1

# itemCheck, outIndex = SearchNode1("T", LinkedList, FreePointer)

# Method 2 - Searching via linked list's order:
def SearchNode2(SearchItem, LinkedList, StartPointer):

    SearchPointer = StartPointer
    while SearchPointer != -1:
        if LinkedList[SearchPointer].NodeData == SearchItem:
            return True, SearchPointer
        else:
            SearchPointer = LinkedList[SearchPointer].NodePointer
    return False, SearchPointer

itemCheck, outIndex = SearchNode2("C", LinkedList, StartPointer)

if itemCheck == True:
    print(f"Item found at: {outIndex}")
else:
    print(f"Item not found!")
print()

# Writing a procedure to delete a node from an ordered linked list:
def DeleteNode(DeleteItem, LinkedList, StartPointer, FreePointer):

    CurrentPointer = StartPointer
    itemFound = False

    if CurrentPointer == -1:
        print("List is empty!")

    else:
        while (itemFound == False and CurrentPointer != -1):
            if DeleteItem == LinkedList[CurrentPointer].NodeData:
                itemFound = True
                LinkedList[CurrentPointer].NodeData = "null"

            else:
                PreviousPointer = CurrentPointer
                CurrentPointer = LinkedList[CurrentPointer].NodePointer
    
    if itemFound == True:
        if CurrentPointer == StartPointer:
            StartPointer = LinkedList[CurrentPointer].NodePointer

        else:
            LinkedList[PreviousPointer].NodePointer = LinkedList[CurrentPointer].NodePointer

        LinkedList[CurrentPointer].NodePointer = FreePointer
        FreePointer = CurrentPointer

    else:
        print("Item not found!")

    return LinkedList, StartPointer, FreePointer

LinkedList, StartPointer, FreePointer = DeleteNode("P", LinkedList, StartPointer, FreePointer)
print("Linked List after an item is deleted:")
OutputList(LinkedList, FreePointer)

# Writing a procedure to output all elements of the linked list in an ordered way:
def OrderedOutput(LinkedList, StartPointer):

    CurrentPointer = StartPointer
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer].NodeData)
        CurrentPointer = LinkedList[CurrentPointer].NodePointer

print()
print("Ordered output of linked list elements (using iteration): ")
OrderedOutput(LinkedList, StartPointer)

# Writing a recursive procedure to output all elements of the linked list in an ordered way:
def recursiveOrderedOutput(LinkedList, StartPointer):

    CurrentPointer = StartPointer
    # print(LinkedList[CurrentPointer].NodeData)
    if CurrentPointer != -1:
        print(LinkedList[CurrentPointer].NodeData)
        recursiveOrderedOutput(LinkedList, LinkedList[CurrentPointer].NodePointer)

print("Ordered output of linked list elements (using recursion): ")
recursiveOrderedOutput(LinkedList, StartPointer)