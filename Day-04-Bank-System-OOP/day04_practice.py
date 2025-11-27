# Day 4 Practice

# inheritence 
class animal:
    def speak(self):
        print("Animal speaking")

class Dog(animal):
    def speak(self):
        print("Dog barking")

a = animal()
d = Dog()
a.speak()
d.speak()

#..... example 2 

class person:
    def into(self):
        return " i am a person"

class student(person):
    def into(self):
        return " i am a Student"

p = person()
s = student()
print(p.into())
print(s.into())


#......compositon...........

# example 1 

class engine:
    def start(self):
        return "engine has started"
class car:
    def __init__(self):
        self.engine = engine()

    def drive(self):
        return self.engine.start() + "car is moving"

c = car()
print(c.drive())

#..... Example 2 ( composition)

class keyboard:
    def type(self):
        return "keyboard typing"
class mouse:
    def click(self):
        return "mouse clicking"
        
class computer:
    def __init__(self):
        self.keyboard = keyboard()
        self.mouse = mouse()
    def work(self):
        return self.keyboard.type() + "\n" + self.mouse.click()

comp = computer()
print(comp.work())


#.......By composition ( Has-A Relationship )......
# ..... By Inheritence ( Is-A Relationship )

class Engine:
    def useEngine(self):
        return "Engine is used"

class car:
    def __init__(self):
        self.engine = Engine()
        # self.obj = Engine()

    def usecar(self):
        return self.engine.useEngine()

obj = car()
obj.usecar

# ------ IS-A relationship -------
### --- if we want to extented existing functionality wite some more extra functinality then we should go for IS - A relationship

class Human:
    def drinkEat(self):
        return "drink and eat"

class Emp(Human):
    def __init__(self, name,eid):
        self.name = name 
        self.eid = eid 

obj = emp("Ali Sadiq", 11220)
print(obj.drinkEat())


# .... another example 
class Car:
    def __init__(self, carBrand):
        self.carBrand = carBrand 

    def getCar(self):
        print("car brand is", self.carBrand)


class emp:
    def __init__(self, eid, ename, car):
        self.eid = eid 
        self.ename = ename 
        self.car = car 

    def display(self):
        print(self.ename)
        print(self.eid)
        self.car.getCar()

car = Car("CHR")
obj = emp("Ehtisham", 1234, car)
obj.display()
    