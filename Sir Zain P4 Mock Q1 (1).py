class ExaminationPaper:
    def __init__(self,centrenum,candnum):
        self.__PaperID=centrenum+candnum #PaperID as String
        self.__FinalMark=0 #FinalMark as Integer
        self.__Grade="Fail" #Grade as String
    def GetFinalMark(self):
        return self.__FinalMark
    def GetGrade(self):
        return self.__Grade
    def GetPaperID(self):
        return self.__PaperID
    def SetFinalMark(self,Mark):
        Mark=int(Mark)
        if Mark>=0 and Mark<=90:
            self.__FinalMark=Mark
            return True
        else:
            return False
    def SetGrade(self,DistMark,MeritMark,PassMark):
        DistMark=int(DistMark) #DistMark as Integer
        MeritMark=int(MeritMark) #MeritMark as Integer
        PassMark=int(PassMark) #PassMark as Integer
        if self.GetFinalMark()>=DistMark:
            self.__Grade="Distinction"
        elif self.GetFinalMark()>=MeritMark:
            self.__Grade="Merit"
        elif self.GetFinalMark()>=PassMark:
            self.__Grade="Pass"
        else:
            self.__Grade="Fail"            

def Main():
    centrenum=input("Please enter your centre number: ")
    candnum=input("Please enter your candidate number: ")
    mark=int(input("Please enter your mark: "))
    ThisPaper=ExaminationPaper(centrenum,candnum)
    ThisPaper.SetFinalMark(mark)
    ThisPaper.SetGrade(80,70,55)
    grade=ThisPaper.GetGrade()
    print(grade)

Main()