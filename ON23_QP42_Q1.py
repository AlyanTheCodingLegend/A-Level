StackVowel=[str for i in range(100)]
StackConsonant=[str for j in range(100)]

VowelTop=0
ConsonantTop=0

def PushData(letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        if VowelTop<100:
            StackVowel[VowelTop]=letter
            VowelTop+=1
        else:
            print("The stack of vowels is full.")
    else:
        if ConsonantTop<100:
            StackConsonant[ConsonantTop]=letter
            ConsonantTop+=1
        else:
            print("The stack of consonant is full.")      

def ReadData():
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    try:
        file=open("StackData.txt","r")
        line=file.readline().strip()
        while line:
            PushData(line)
        file.close()    
    except FileNotFoundError:
        print("The file is not found.")

def PopVowel():
    global StackVowel
    global VowelTop
    if VowelTop==0:
        return "No data"
    else:
        VowelTop-=1
        return StackVowel[VowelTop]
    
def PopConsonant():
    global StackConsonant
    global ConsonantTop
    if ConsonantTop==0:
        return "No data"
    else:
        ConsonantTop-=1
        return StackConsonant[ConsonantTop]
    
ReadData()    
return_string=[]
for i in range(5):
    user_input=input("Please enter 'vowel' or 'consonant': ").lower()
    if user_input=="vowel":
        returnval=PopVowel()
        if returnval=="No data":
            print("The vowel stack is empty.")
        else:
            return_string.append(returnval)
    elif user_input=="consonant":
        returnval=PopConsonant()
        if returnval=="No data":
            print("The consonant stack is empty.")
        else:
            return_string.append(returnval)    