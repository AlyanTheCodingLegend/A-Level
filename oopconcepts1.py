class className:
    def __init__(self, privP): # constructor
        self.public=0
        self._protected=0 # can access it directly but it is not recommended
        self.__private=privP

    def getPrivate(self):
        return self.__private # I will GET the value of private attribute
    
    def setPrivate(self, privateP):
        self.__private=privateP


temp1 = className(5)

print(temp1.getPrivate()) # should print 5

temp1.setPrivate(9)

print(temp1.getPrivate()) # should print 9

# "HAS-A" = containment / composition
# "IS-A" = inheritance

# inheritance

class ParentClass:
    def __init__(self, atr1P):
        self.atr1=atr1P

class ChildClass(ParentClass):
    def __init__(self,atr1Param,atr2P):
        self.atr2=atr2P
        super().__init__(atr1Param)

# ChildClass IS-A ParentClass Example: Tesla IS-A Car

# containment / composition

class SubClass:
    def __init__(self,atr1P):
        self.atr1=atr1P

class SuperClass:
    def __init__(self, astr1Param):
        self.sub1=SubClass(astr1Param)

# object of the subclass is the attribute of the parent class

# SuperClass HAS-A SubClass Example: Tesla HAS-A Engine

class Employee:
    def __init__(self,id,age,salary):
        self.id=id
        self.age=age
        self.salary=salary

    def giveBonus(self):
        self.salary=self.salary*1.2 # 20% increase in salary

    def giveBonus(self, perc):
        self.salary=self.salary*(1+perc)

class Director(Employee):
    def __init__(self,id,age,salary, name):
        super().__init__(id,age,salary)
        self.name=name

    def giveBonus(self):
        self.salary=self.salary*1.4 # 40% increase in salary

# method overriding = polymorphism = have same method with same name and parameters in two different classes
# method overloading = have same method name with different number of parameters


