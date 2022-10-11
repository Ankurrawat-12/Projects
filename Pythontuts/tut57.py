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
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @classmethod
    def from_slash(cls, string):
        return cls(*string.split("/"))


ankur = Employee("Ankur", 500, "Instructor")
harry = Employee("Harry", 255, "Student")
karan = Employee.from_dash("Karana-480-Student")
arjun = Employee.from_slash("Arjun/480/Student")

print(karan.no_of_leaves)
print(arjun.name)
harry.change_leaves(34)

print(ankur.no_of_leaves)
