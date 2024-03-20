# file = open(filename, mode)

# file organization: serial, sequential, random
# file access: sequential, direct

import pickle

class Human:
    def __init__(self,id,name,eyecol):
        self.id=id # key-field = UNIQUE
        self.name=name
        self.eyecol=eyecol

human1=Human(908420328, "Alyan", "black")

binaryfile = open("aBinaryFile.dat","wb+")

address=hash(human1.id) # address unique

binaryfile.seek(address) # relocate cursor to record insertion point

pickle.dump(human1,binaryfile) # writing process

# objects -> bytes, bytes are written to binary file / pickling ya serializing
# bytes -> objects, returns object / deserialization

# id = 90848109238012
# hash = 0984309248123

address=hash("sdbfjkfdbjksdfew")
binaryfile.seek(address)
record=pickle.load(binaryfile) # reading process
print(f"Name: {record.name}") # computation with the record

binaryfile.close()


