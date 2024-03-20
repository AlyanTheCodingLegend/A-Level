TwoDArrayDuplicate=[["" for col in range(3)]for row in range(10)]

def SearchFileNtoZ(filename,accnum):
    filehandle=open(filename,"r")
    temp="1"
    found=False
    while len(temp)!=0:
        temp=filehandle.readline()
        for i in range(len(temp)):
            if temp[i]=="*":
                count=i
                break
        if temp[0:count]==accnum:
            found=True
    return found
    filehandle.close()
      
    
def FindDuplicates():
    global TwoDArrayDuplicate
    filehandle=open("UserListAtoM.txt","r")
    filehandle2=open("FileDuplicates.txt","w")
    temp="1"
    found=False
    while len(temp)!=0 and found==False:
        temp=filehandle.readline()
        for i in range(len(temp)):
            if temp[i]=="*":
                count=i
                break
        accnum=temp[0:count]
        for i in range(count+1,len(temp)):
            if temp[i]=="*":
                count2=i
                break
        name=temp[count+1:count2]
        telenum=temp[count2+1:len(temp)]    
        found=SearchFileNtoZ("UserListNtoZ.txt",accnum)
    if found==True:
        filehandle2.write(accnum)
        TwoDArrayDuplicate[0][0]=accnum
        TwoDArrayDuplicate[0][1]=name
        TwoDArrayDuplicate[0][2]=telenum

    filehandle.close()
    filehandle2.close()    

    
FindDuplicates()
print(TwoDArrayDuplicate)