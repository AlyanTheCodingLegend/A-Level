x="HeLoIu"
x=x.upper()
print(x)
filehandle=open("DataToAdd.txt","r")
for i in range(11):
    temp=filehandle.readline()
    print(temp)
    print(len(temp))