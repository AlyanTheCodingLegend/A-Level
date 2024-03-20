values=int(input("How many values of this sequence do you want?"))
num1=int(1)
num2=int(1)
print(num1)
print(num2)
for i in range(1,values-1):
    num3=int(num1+num2)
    num1=num2
    num2=num3
    print(num3)