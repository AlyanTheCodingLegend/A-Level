sum=0
numbers=input("Enter numbers with blank: ")

list=numbers.split()
print(list)

for i in range(len(list)):
    list[i]=int(list[i])
    if list[i]==5 or list[i]==3:
        sum+=list[i]

print(sum)        