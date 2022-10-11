# Static Methods In Python

# Class Methods As Alternative Constructors

# Class Methods In Python

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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @classmethod
    def from_slash(cls, string):
        return cls(*string.split("/"))

    @staticmethod
    def print_good(string):
        print("This is good "+string)
        # return "69"

ankur = Employee("Ankur", 500, "Instructor")
harry = Employee("Harry", 255, "Student")
karan = Employee.from_dash("Karana-480-Student")
arjun = Employee.from_slash("Arjun/480/Student")

print(karan.no_of_leaves)
print(ankur.no_of_leaves)
# ankur.print_good("boy ankur")
Employee.print_good("boy Ankur")
# print(ankur.print_good("boy ankur"))
