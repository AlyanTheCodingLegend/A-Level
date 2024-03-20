import pickle

class human:
    def __init__(self,i,e,h,a,d,w):
        self.id=i # key field=unique
        self.eyecol=e
        self.name=h
        self.age=a
        self.dob=d
        self.weight=w

zain1=human(817321098,"black","zain",19,"12th june 2019",65.4)
file=open("amazingfile.dat","wb")

# pickle.dump(object,file)

address=hash(zain1.id) # UNIQUE
file.seek(address)
pickle.dump(zain1,file) 

file.close()
def get_record(keyfield_id):
    file=open("amazingfile.dat","rb")
    address=hash(keyfield_id)
    file.seek(address)
    record=pickle.load(file)
    print(record.name)
    file.close()


get_record(817324234)    





