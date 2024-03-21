# SCREEN NAZAR AARAHI?

# parent class banatey hain

class LivingThing:
    def __init__(self,age, eyecol):
        self.age=age
        self.eyecol=eyecol

    def make_sound(self):
        print("WHATS UP! I DO BE LIVING")

# ab child class

class Human(LivingThing):
    def __init__(self, age, eyecol, name, cnic):

        super().__init__(age,eyecol) # inherit the properties of the SUPER/ PARENT CLASS
        self.name=name
        self.cnic=cnic

    def make_sound(self): # polymorphism
        print("INSAAN HOON MEIN!")

# BASICALLY, WE MADE A METHOD WITH EXACTTT SAME NAME IN TWO CLASSES, AT THE MOMENT PARENT AND CHILD CLASS ARENT CONNECTED
        # we shall connect em first so lets do ALLDAT 

        # NOW, THE CLASS HUMAN INHERITSS TWO ATTRIBUTES FROM LIVING TING
        # SINCE LIVING THING HAS ATTRIBUTES WHICH ALSO BELONG TO HUMAN
        # SUPER BASICALLY CALLS THE CONSTRUCTOR OF THE PARENT CLASS.


        # YEH HAI SYNTAX, when u write super, it calls constructor (__init__) of Parent class (class inside brackets)

alyan = Human(19, "black", "Alyan", 173197381931)

# alyan.make_sound()

# WAITTT
# i think im messing up the order of constructors, gimme 2 mins

# dekho, I FOUND THE ISSUE, look carefully and acknowledge
# bas brackets laganey ka scene tha

# SIRF TWO ATTRIBUTES HOONGEY LIVING THING WAALEY, CUZ DOG AINT A HUMAN
dog = LivingThing(498, "idek lmao")
dog.make_sound()

# CORRECT

# nononono, polymorphism is basically method/ functions overloading, we made methods of exact same names, and with parent/child classes, the same method performs differently

# YESSS, inheritance bhi issi mein hai, linking classes with super was inheritance

# yes, used saath mein. ab yehi scheme hai ke parent class has extremely generic attributes and the specific child class inherits those attributes, plus it has its own SPECIFIC attributes, then we do method voerloading if we want child class to perform more specifically

# cuz dekho, even a Human can say WHATUP IM LIVING, but saying, INSAAN HOON MEIN is way better, in other cases polymorphism is required to calculate stuff case-wise

# TIME FOR NEXT EXAMPLE


# CAR HAS A ENGINE
# PARENT HAS A CHILD (containment, composition)

class Engine:
    def __init__(self,oilcapacity):
        self.oilcapacity=oilcapacity

class Car:
    def __init__(self, name):
        self.name=name
        self.engine=Engine(-1) # composition

    def sound(self):
        print("VROOOM")

class Tesla(Car):
    def __init__(self, name, batterycapacity):
        super().__init__(name)
        self.batterycapacity=batterycapacity

    def sound(self):
        print("........IM AN ELECTRIC CAR")

class Buggati(Car):
    def __init__(self, name, horsep):
        
        super().__init__(name)
        self.horsep=horsep

    def sound(self):
        print("I WOKE UP IN A NEW BUGG-")

modelS=Tesla("MODEL S", 8121)
superSport=Buggati("SUPER SPORT 16.4", 231)

modelS.sound()
superSport.sound()

# AB AIK AUR CASE HAI, dekho we just inherited stuff, I COULD SAY KE Car and TESLA have a "IS-A" relationship because TESLA "IS-A" Car, u get me?? child IS A parent
# second type of relation is "HAS-A", usmein aik class contains object of another class, ab IS-A is inheritance, HAS-A is containment / composition

# IGHT, LETS GOOO, example time

# yaar dekho, in the case of private, do make sure ke u have getters and setters for attributes, baqi methods(functions) are public by default in python, java has MADDD customisability for OOP, usmein methods can ALSO have private type, even tho thats retarded cuz method ko access karney ke liye aik aur getter setter chahiye hogalmaooo
# as for ur question, depends on the caie ka queston (literally hahah)
# ukw, chalo private sey kartey 

class CookingInstruction:
    def __init__(self, difficulty, actualinstruction, duration):
        self.__difficulty=difficulty
        self.__act=actualinstruction
        self.__duration=duration

    def getInstruction(self): # GETTER
        return self.__act
    
    def setDifficulty(self, difficulty): # SETTER
        self.__difficulty=difficulty
    
class Ingredients:
    def __init__(self, name, amount):
        self.__name=name
        self.__amount=amount

    def getIng(self):
        return self.__name+" "+self.__amount

instr1=CookingInstruction("MEDIUM", "BOIL WATER FOR 5 MINS", 5)
instr1.setDifficulty("Super easy") 

# setters literally set the value of attributes
# getters literally get the value of attributes

class Recipe:
    def __init__(self, name):
        self.__name=name
        self.__instructions=[CookingInstruction("unknown","",-1) for i in range(10)] # we r storing 10 empty cooking instructions inside each recipe
        self.__ingredients=[Ingredients("",-1) for i in range(20)] # maximum 20 ingredients hosaktey

    def getInstructions(self):
        for i in range(10):
            if (self.__instructions[i].getInstruction()!=""):
                print(self.__instructions[i].getInstruction())    # this will work cuz private attribute hai so we shall use the getter method to extract string waala instruction

    def getIngredient(self):
        for i in range(20):        
            print(self.__ingredients[i].getIng())

    def addInst(self, instruction):
        for i in range(len(self.__instructions)):
             # DONT DO THIS WAISEY IN ALL CASES CUZ THIS J MAKES A NEW SPACE (AN 11TH ONE IF U MAY), we should actually find an empty space in the pre-defined array then add instruction there        
            if self.__instructions[i].getInstruction()=="":
                self.__instructions[i]=instruction
                break
                 # SAMAJH AARAHA? i basically checked if an instruction had empty body phir udhar store krdiya
# ab heres another problem, to actually store instructions and ingredients, we shall need setters            

    # UKW, LEMME J DO DAT    
                
chickentikkamasala=Recipe("Chicken Tikka Masala")
chickentikkamasala.addInst(CookingInstruction("Easy", "First let the water boil", "20 minute"))

chickentikkamasala.getInstructions()

# bilkul aa sakta,u wont find it in past papers (with inheritance and polymorphism included)

# haan, inheritance came in my paper and then next paper too
# ajao sawaal time
# yes concepts done

# lets do my paper (mujhsey q3 caie mein shi nhi huwa tha, but ez A* so meh)
# gimme 2 mins, dhoond ke nikalta paper
# check the link, on discord, best, lets do question 3 uska
# yes correct

# mon-fri
# tues, thurs
# thurs -> friday
# tues, fri, sat (10 am)

