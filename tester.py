list1 = [2,3,2,1,6,7,8]

#list1[5] # gives 7

#list1.append(9)

print(list1[2:5]) # will give index position 2 and 3 and 4 ki list

# starting index is inclusive, ending index is exclusive, this is python's DEFAULT behaviour

tempo = "hello world"
char = "d"

for i in range(len(tempo)): # 0 - 11
    if char==tempo[i]:
        print(i)

for i in range(2,5):
    print(list1[i])

from random import randint

print(randint(1,10))

# import random
# import pickle
# import os (optional)
# from datetime import datetime

from datetime import datetime
print(datetime.now())
