import pickle

file = open("temp123.txt", "a+")

def writetofile():
    global file
    for _ in range(10):
        file.write("Hello World\n")

def readfromfile():
    global file # go to start of file
    for _ in range(10):
        print(file.readline())

writetofile()

file.close()

file = open("temp123.txt", "a+")

readfromfile()   

file.close()

# file.write("Hello World\n")
# int(file.readline().strip())

# file.seek(0)
# # file.tell()

# address=hash(id)
# file.seek(address)

# file.write("Hello World\n")

# file=open("binaryfile.dat", "ab+")
# pickle.dump("Hello World", file)
# pickle.load(file)

# file.close()

