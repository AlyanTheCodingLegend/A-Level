def Unknown(x,y):
    x=int(x)
    y=int(y)
    if x<y:
        print(x+y)
        return (Unknown(x+1,y))*2
    else:
        if x==y:
            return 1
        else:
            print(x+y)
            return int((Unknown(x-1,y)/2))
        
print("10 and 15")
val=Unknown(10,15)
print(val)
print("10 and 10")
val2=Unknown(10,10)
print(val2)
print("15 and 10")
val3=Unknown(15,10)
print(val3)

def IterativeUnknown(x,y):
    count=0 #count is an exponential factor of 2
    x=int(x)
    y=int(y)
    while x!=y:
        if x<y:
            print(x+y)
            x+=1
            count+=1
        else:
            print(x+y)
            x-=1 
            count-=1
    val=2**count
    return int(val)
        
print("10 and 15")
val=IterativeUnknown(10,15)
print(val)
print("10 and 10")
val2=IterativeUnknown(10,10)
print(val2)
print("15 and 10")
val3=IterativeUnknown(15,10)
print(val3)

print(IterativeUnknown(4,6))