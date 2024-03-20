import datetime
class Character:
    def __init__(self,n,b,i,s):
        self.__CharacterName=n
        self.__DateOfBirth=b
        self.__Intelligence=i
        self.__Speed=s
    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
    def SetIntelligence(self,intelligence):
        self.__Intelligence=intelligence
    def Learn(self):
        self.__Intelligence*=1.1
    def ReturnAge(self):
        age=2023-int(self.__DateOfBirth[-4:])
        return age
    
FirstCharacter=Character("Royal","1 January 2019",70,30)
FirstCharacter.Learn()
print(f'Name: {FirstCharacter.GetName()} Age: {FirstCharacter.ReturnAge()} Intelligence: {FirstCharacter.GetIntelligence()}')    


class MagicCharacter(Character):
    def __init__(self,e,n,b,i,s):
        self.__Element=e
        super().__init__(n,b,i,s)
    def Learn(self):
        if self.__Element=="fire" or self.__Element=="water":
            intelligence=super().GetIntelligence()
            intelligence*=1.2
            super().SetIntelligence(intelligence)
        elif self.__Element=="earth":
            intelligence=super().GetIntelligence()
            intelligence*=1.3
            super().SetIntelligence(intelligence)
        else:
            intelligence=super().GetIntelligence()
            intelligence*=1.1
            super().SetIntelligence(intelligence)
    def ReturnAge(self):
        age=2023-self.__DateOfBirth
        return age


FirstMagic=MagicCharacter("Light",2018,75,22,"fire")
FirstMagic.Learn()
print(f'Name: {FirstMagic.GetName()} Age: {FirstMagic.ReturnAge()} Intelligence: {FirstMagic.GetIntelligence()}')        
 

        