class Employee:
    def __init__(self, payP, numberP, jobTitleP):
        self.__HourlyPay = payP  # REAL
        self.__EmployeeNumber = numberP  # STRING
        self.__JobTitle = jobTitleP  # STRING 
        self.__PayYear2022 = [0.0 for _ in range(52)]  # DECLARE PayYear2022: ARRAY[0:51] OF REAL


    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    
    def SetPay(self, weekNumber, hoursWorked):
        weekPay = self.__HourlyPay * hoursWorked
        self.__PayYear2022[weekNumber - 1] = weekPay


    def GetTotalPay(self):
        total = 0
        for i in range(len(self.__PayYear2022)):
            total = total + self.__PayYear2022[i] 

        return total


class Manager(Employee):
    def __init__(self, bonusP, payP, numberP, jobTitleP):
        self.__BonusValue = bonusP
        super().__init__(payP, numberP, jobTitleP)
    
    def SetPay(self, weekNumber, hoursWorked):
        hoursWorked = (hoursWorked * (self.__BonusValue/100)) + hoursWorked 
        super().SetPay(weekNumber, hoursWorked)

EmployeeArray=[]
# DECLARE EmployeeArray: ARRAY[0:7] OF Employee

try:
    file=open('Employees.txt','r')
    for i in range(8):
        try:
            hourlyPay=float(file.readline().strip())
            empNum=file.readline().strip()
            temp=file.readline().strip()
            bonusVal = float(temp)
            # if no error, Manager
            jobTitle=file.readline().strip()
            EmployeeArray.append(Manager(bonusVal,hourlyPay,empNum,jobTitle))
        except ValueError:
            # if error, Employee
            jobTitle=temp
            EmployeeArray.append(Employee(hourlyPay, empNum,jobTitle))

    file.close()
except FileNotFoundError:
    print('The file was not found')    

def EnterHours():
    try:
        file=open('HoursWeek1.txt','r')
        for i in range(8):
            empNum=file.readline().strip()
            numHours=float(file.readline().strip())

            for i in range(8):
                if empNum==EmployeeArray[i].GetEmployeeNumber():
                    EmployeeArray[i].SetPay(1,numHours)
                    break
        
        file.close()
    except IOError:
        print('File not found')

EnterHours()

for i in range(8):
    print(f'Employee Number: {EmployeeArray[i].GetEmployeeNumber()} - Total Pay: {EmployeeArray[i].GetTotalPay()}')