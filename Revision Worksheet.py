ErrCode=[int for i in range(500)]
ErrText=[str for i in range(500)]
for i in range(500):
    ErrCode[i]=999
    ErrText[i]="<Undefined>"

ErrCode[0]=10
ErrCode[1]=25
ErrCode[2]=30
ErrCode[3]=999
ErrCode[4]=40
ErrCode[5]=55
ErrCode[6]=999
ErrCode[7]=70
ErrCode[8]=85
ErrCode[9]=90
ErrText[0]="Invalid identifier name"
ErrText[1]="Bracket mismatch"
ErrText[2]="Undeclared variable"
ErrText[3]="<Undefined>"
ErrText[4]="Type mismatch in assignment"
ErrText[5]="Invalid Operator"
ErrText[6]="<Undefined>"
ErrText[7]="Initialisation missing"
ErrText[8]="Invalid keyword"
ErrText[9]="Invalid variable"

def OutputError(linenum,errornum):
    found=False
    for i in range(500):
        if ErrCode[i]==errornum:
            print(f'{ErrText[i]} on line {linenum}')
            found=True
            break
    if found==False:
        print(f'Unknown error on line {linenum}')

OutputError(70,30)
OutputError(35,60)

def SortArrays():
    global ErrCode,ErrText
    for i in range(1,500):
        key=ErrCode[i]
        key2=ErrText[i]
        j=i-1
        while j>=0 and key<ErrCode[j]:
            ErrCode[j+1]=ErrCode[j]
            ErrText[j+1]=ErrText[j]
            j=j-1
        ErrCode[j+1]=key 
        ErrText[j+1]=key2   
       

SortArrays()
print(ErrCode)
print(ErrText)








