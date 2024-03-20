'''
def Unknown(x,y):
    if x<y:
        print(x+y) # 25-29
        return (Unknown(x+1,y))*2 # reason for getting 32
    else:
        if x==y:
            return 1
        else:
            print(x+y)
            return (Unknown(x-1,y)//2)
print("Recursive: ")
print("Paremeters x=10 y=15")        
print(f"Answer 1: {Unknown(10,15)}")
print("Paremeters x=10 y=10")        
print(f"Answer 2: {Unknown(10,10)}")
print("Paremeters x=15 y=10")        
print(f"Answer 3: {Unknown(15,10)}")
print("\n")

def IterativeUnknown(x,y):
    total=1 # return value
    if x<y:
        while x!=y:
            print(x+y)
            x=x+1
            total=total*2
    elif x>y:
        while x!=y:
            print(x+y)
            x=x-1
            total=total//2
    return total                

print("ITERATIVE: ")
print("Paremeters x=10 y=15")        
print(f"Answer 1: {IterativeUnknown(10,15)}")
print("Paremeters x=10 y=10")        
print(f"Answer 2: {IterativeUnknown(10,10)}")
print("Paremeters x=15 y=10")        
print(f"Answer 3: {IterativeUnknown(15,10)}")


def IterativeUnknownTwo(x,y):
    total=1
    factoroftwo=0 
    if x<y:
        while x!=y:
            print(x+y)
            x=x+1
            factoroftwo+=1
    elif x>y:
        while x!=y:
            print(x+y)
            x=x-1
            factoroftwo-=1

    return int(total*(2**factoroftwo))

print(f"Answer: {IterativeUnknownTwo(10,15)}")

'''



def recursive_summation(number):
    if number==1:
        return 1
    else:
        return number+recursive_summation(number-1)
    
Pre order