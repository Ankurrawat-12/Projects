# Public, Private & Protected Access Specifiers

"""
Public :-
Protected :-
Private :-
"""


class Employee:
    no_of_leaves = 8
    # var = 8 2nd
    public = "Public variable"
    _protect = "protected variable"
    __private = "private variable"

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


ankur = Employee("Ankur", 88000, "Programmer")
print(ankur._protect)
# print(ankur.__private)  # 'Employee' object has no attribute '__private'
print(ankur._Employee__private)