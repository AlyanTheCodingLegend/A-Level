# CONSTRCUTOR TIME

class Employee:
    def __init__(self, hourly,empnum, title):
        self.__HourlyPay=hourly
        self.__EmployeeNumber=empnum
        self.__JobTitle=title 
        self.__PayYear2022=[0.0 for i in range(52)]

        # i think its done now

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber # ab dekho, in this q im not sure if they metioned ke the attr are private but meney orivate liye cuz i could clearly see ke aagey jaakey getters setters bananey hain so do keep this in mind

    def SetPay(self,weeknum, hoursnum):
        pay=self.__HourlyPay*hoursnum
        self.__PayYear2022[weeknum-1]=pay # array index starts from 0, week num tou 1 sey start hoga na, logical si baat hai 
         # Done ig

    def GetTotalPay(self):
        total=0.0
        for i in range(52): # range ko directly 52 bhi kr saktey
            total+=self.__PayYear2022[i]
        return total    
         # done again
    
# child class time, idhar merey lagey thhey
# indeed
    
    # WTF, FILE KA SAWAAL BHI TOU THA ISMEIN, HELL NAWW

# yes, but we move
        
        # ajao class code krtey yeh waali
    
class Manager(Employee):
    def __init__(self, bonusval, hourlypay, empnum, title):
        self.__BonusValue=bonusval
        super().__init__(hourlypay, empnum, title)
         # done ?

    def SetPay(self,weeknum,numofhours):
        super().SetPay(weeknum,numofhours*(1+(self.__BonusValue/100)))
        # i think increase aisey hi krna hai, ya wait, percentage mein convert kreingey 
        # we'll recheck this later

        # BESTTT

# okay, time for the ajeeb part
# part (c)

# lemme cop the Employees.txt file

# okay, so the third line in each record will either be title or bonus value (lets apply try except block here)


EmployeeArray=[]

# samajh aaraha?

# we made an array and then opened a file for reading
# next we loop dis

try:
    file=open("Employees.txt", "r")
    for i in range(8): # ignore this loop for now, bas understand ke this loop will read all lines in the file
        
            hourlypay=float(file.readline().strip())
            empnum=file.readline().strip()
            temp=file.readline().strip()
            # either bonus val or job title
            # we assume bonus val taakey agar na ho tou error ajaye
            try:
                bonusval=float(temp) # error
                jobtitle=file.readline().strip()
                EmployeeArray.append(Manager(bonusval,hourlypay,empnum,jobtitle))
            except ValueError:
                # no, ismein error yeh hoga we r converting 3rd line to float (bonusvalue) waali, ab if its jobtitle it wont be converted to float and error aayega, konsa error aayega yeh mein dekh ke batata
                jobtitle=temp
                EmployeeArray.append(Employee(hourlypay,empnum,jobtitle))

            # i think this question is generally done, we shall check it later when testing
    file.close()    
except FileNotFoundError:
    print("File not found!")
# part (d)


def EnterHours():
    try:    
        file1=open("HoursWeek1.txt","r")
        for i in range(8): # again, ignore the range rn
            empnum=file1.readline().strip()
            numofhours=float(file1.readline().strip())
            for j in range(8):
                if empnum==EmployeeArray[j].GetEmployeeNumber():
                    EmployeeArray[j].SetPay(1, numofhours) # 1 is weeknum, ooper sawaal mein they said ke week 1 ki details hain yeh
                    break
        
        file1.close()
    except IOError:
        print("File not found!!")    

# testing phase, part (e)
    
EnterHours()
for i in range(8):
    print(f"Employee Number: {EmployeeArray[i].GetEmployeeNumber()} Total Pay: {EmployeeArray[i].GetTotalPay()}")    

# i think ke ghalti hogi koi but we'll fix it
    
    # file ka naam was file1

    # HOLD UP, yeh kya ho raha, hold up

    # wait, loop check kareingey matlab
 # we got smth, i think merey caie mein bhi yehi output aaraha tha mera lmaoo
     # still got dat skill issue fr
    
    # lets debug
    