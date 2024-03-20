def IterativeCalculate(Number):
    # Total as integer
    # ToFind as integer
    ToFind=Number
    Total=0
    while Number!=0:
        if ToFind%Number==0:
            Total+=Number
        Number-=1
    return Total        

print(f"The return value of function with parameter '10' is: {IterativeCalculate(10)}")

def RecursiveValue(Number, ToFind):
    if Number==0:
        return 0
    else:
        if ToFind%Number==0:
            return Number+RecursiveValue(Number-1,ToFind)
        else:
            return RecursiveValue(Number-1,ToFind)
        
print(f"The return value of recursive function with parameters '50' and '50'  is: {RecursiveValue(50,50)}")        