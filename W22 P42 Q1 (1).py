global Jobs
global NumberOfJobs
Jobs=[[0 for i in range(2)] for j in range(100)]
#DECLARE NumberOfJobs:INTEGER

def Initialize():
    global Jobs
    global NumberOfJobs
    NumberOfJobs=0
    for i in range(2):
        for j in range(100):
            Jobs[j][i]=-1

def AddJob(jobnum,priority):
    global Jobs
    global NumberOfJobs
    jobnum=int(jobnum)
    priority=int(priority)
    if NumberOfJobs<100:
        Jobs[NumberOfJobs][0]=jobnum 
        Jobs[NumberOfJobs][1]=priority
        NumberOfJobs+=1
        print("Added")
    else:
        print("Not added")          

Initialize()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(1,NumberOfJobs):
        key=Jobs[i][1]
        key2=Jobs[i][0]
        j=i-1
        while j>=0 and key<Jobs[j][1]:
            Jobs[j+1][1]=Jobs[j][1]
            Jobs[j+1][0]=Jobs[j][0]
            j=j-1
        Jobs[j+1][1]=key 
        Jobs[j+1][0]=key2   

def PrintArray():
    global Jobs
    for i in range(NumberOfJobs):
        jobnum=str(Jobs[i][0])
        jobpri=str(Jobs[i][1])
        print(jobnum+" priority "+jobpri)

InsertionSort()
PrintArray()        
