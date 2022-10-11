# Operator Overloading & Dunder Methods

"""
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and roll is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    #Dunder methods
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return self.printdetails()


emp1 = Employee("Ankur", 610, "Programmer")
# emp2 = Employee("Rohan", 55, "Cleaner")
# print(emp1 + emp2)
# print(emp1 / emp2)

# print(str(emp1))  # Will show str if it is present else will show repr
print(emp1)  # -> Will show str if it is present else will show repr
print(repr(emp1))  # -> Will show  repr
"""
# Quiz
class Cat:
    def __init__(self, Name, color, owner):
        self.name = Name
        self.color = color
        self.owner = owner

    def __add__(self, other):
        return self.name + " and " + other.name

    def __eq__(self, other):
        return f"{self.name} and {other.name} are obviously not the same. They're cats, not integers."

    def __ne__(self, other):
        return f"{self.name} and {other.name} aren't equal!!!! They're cats brah."

    def __str__(self):
        return f"\nName is {self.name}\nColor is {self.color}\nOwner is {self.owner}."


mskitty = Cat("MsKitty", "Orange and black", "Pakhi")
laura = Cat("Laura", "Black", "Artemis")
bast = Cat("Bast", "Yellow and Grey", "Nathan")

print(laura + bast)
print(mskitty == laura)
print(mskitty != laura)
print(bast)
print(mskitty)