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


ankur = Employee("Ankur", 455, "Instructor")
harry = Employee("Harry", 255, "Student")

# Employee.change_leaves(34)
ankur.change_leaves(34)

print(ankur.no_of_leaves)
