import pickle
class car:
    def __init__(self):
        self. vehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.purchase = 0.00

myCars = [car() for i in range(100)]
for i in range(100):
    myCars[i].vehicleID = i+1

fileHandle = open("carfile.DAT", "wb")
for i in range(100):
    print(i)
    pickle.dump(myCars[i],fileHandle)

fileHandle.close()

readHandle = open("carfile.DAT", "rb")
ourCars = []
moreLines = True
i = 0
while moreLines:
    try:
        ourCars.append(pickle.load(readHandle))
        print(i)
        i+=1
    except EOFError:
        print("file read till the end")
        moreLines = False

for i in range(100):
    print(i)
    print(ourCars[i].vehicleID)
readHandle.close()