# iterative loops
# for loop, while loop
# 1 set of recursion logic replaces 1 for/while loop

# a set of recursion logic contains 3 things: base case (condition at which program has to terminate, recursion has to STOP), general case(formula which we use to perform recursion), calling function(when we call the same function that we are defining)

def iterative_factorial(number):
    temp=number
    result=1

    if number>1:
        while temp>1:
            result=result*temp
            temp-=1

        return result    
    else:
        return 1
    

def recursive_factorial(number):
    # base case: number=0
    # general case: result * (result-1)! = result!
    # general case in terms of function calls: f(num) = num*f(num-1)

    if number==0: # if base case: return base value
        return 1
    else: # else: return general case in terms of function calls
        return number*recursive_factorial(number-1)

    # 5! = 5*4!
    # 4!= 4*3*2*1

# number: 5
# f(5) = 5*f(4) winding, these function calls are winded/pushed onto a stack (Last in, First out)
# f(4) = 4*f(3)
# f(3) = 3*f(2)
# f(2) = 2*f(1)
# f(1) = 1*f(0)
# f(0) = 1
# f(1) = 1*1 =1 unwinding, these function calls are popped once a constant value (not a function call) is determined
# f(2) = 2*1 =2
# f(3) = 3*2 =6
# f(4) = 4*6 =24
# f(5) = 5*24 = 120

# 0, 1, 1, 2, 3, 5, 8, 13, 21..............
# term3: 1(doosra one), temp: 1(pehla one), term2: 1(doosra one), term1: 1(pehla one)

def iterative_fib(numberofterms):
    term1=0
    term2=1
    temp=-1
    term3=-1

    result=str(term1)+", "+str(term2)+", "

    if numberofterms==1:
        return str(term1)
    elif numberofterms==2:
        return f"{term1}, {term2}, "
    else:
        for _ in range(numberofterms-2):
            term3=term1+term2
            temp=term2
            term2=term3
            term1=temp
            result=result+str(term3)+", "

        return result    

print(iterative_fib(9))

def recursive_fib(term1, term2, numberofterms):
    # two base cases: same as iterative solution
    
    result=str(term1)+", "+str(term2)+", "

    if numberofterms==1:
        return str(term1)
    elif numberofterms==2:
        return result
    else:
        if numberofterms>0:
            result+=recursive_fib(term2, term1+term2, numberofterms-1)
        else:
            return result   

def recursive_fib(term1, term2, numberofterms):
    # Base case: if numberofterms is 1, return term1
    if numberofterms == 1:
        return str(term1)
    # Base case: if numberofterms is 2, return both term1 and term2
    elif numberofterms == 2:
        return str(term1) + ", " + str(term2)
    # If numberofterms is greater than 2, generate Fibonacci sequence recursively
    else:
        # Generate the next term
        term3 = term1 + term2
        # Recursively call the function with updated terms and decremented numberofterms
        return str(term1) + ", " + recursive_fib(term2, term3, numberofterms - 1)
 
        
print(recursive_fib(0,1,9))

# term 3: 1
# f(0,1,4) = 0, f(1,1,3)
# term 3: 2
# f(1,1,3) = 1, f(1,2,2)
# f(1,2,2) = 1, 2

# winding is complete, unwinding time

# f(1,1,3) = 1, 1, 2
# f(0,1,4) = 0, 1, 1, 2



