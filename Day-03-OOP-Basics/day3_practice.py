# pyhton obnejct oriented programimg 

#... when I say data and functions that are associated with a specific class is called object 
# ... methode = I   mean a function that is associated with a class 

class Employee:

    def putdata(self):
        self.id = int(input("Enter the id : "))
        self.name = input("Enter the name : ")
        self.salary = int(input("Enter the salary : "))

    def display(self):
        print(f"empolyee id :{self.id}")
        print(f"empolyee name :{self.name}")
        print(f"empolyee salary :{self.salary}")

a = Employee()
a.putdata()
a.display()



# second example 
#... class tempalate 
class First:
    x = 50 

obj = First()
print(obj.x)

# ... example 4 

class Employee:
    pass

emp1 = Employee()
emp2 = Employee()
print(emp1)
print(emp2)

emp1.first = "Ali "
emp1.last = "Sadiq"
emp1.mail = "Alisadiq@gmail.com"
emp1.salary = 100000000


emp2.first = "Etisham "
emp2.last = "Sadiq"
emp2.mail = "Etishamsadiq@gmail.com"
emp2.salary = 100000000

print(emp1.mail)
print(emp2.mail)

# this is a bad pratice 

class Employee:
    def __init__(self, first , last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.mail = first + "." + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"

emp1 = Employee("Ali", "Sadiq", 100000000)
emp2 = Employee("Etisham", "Sadiq", 100000000)
print(emp1.fullname())
print(emp2.fullname()) 

# how to pass parameters to a class 

class faculty:
    def __init__ (self, a,b,c):
        self.f_id = a
        self.f_name = b
        self.f_salary = c

    def display(self):
        print(f"faculty id :{self.f_id}")
        print(f"faculty name :{self.f_name}")
        print(f"faculty salary :{self.f_salary}")
    a = faculty(1, "Ali", 100000000)
    a.display() 
    


# example 

class Employee:
    companyName = "Apple"

    def __init__(self, name ):
        self.name = name 
        self.raise_amount = 0.02

    def showDetail(self):
        print(f"the name of the emlopyee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

    emp1 = Employee("Ali")
    emp1.raise_amount = 0.05
    emp1.showDetail()
    emp2 = Employee("Etisham")
    emp2.showDetail()
    emp2.raise_amount = 0.03
    emp2.showDetail()