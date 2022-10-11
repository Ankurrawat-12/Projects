# Self & __init__() (Constructors)


class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and roll is {self.role}"


ankur = Employee("Harry", 455, "Instructor")
# harry = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# ankur.name = "Ankur"
# ankur.salary = 4554
# ankur.role = "Head Programmer"
#
# print(ankur.printdetails())
# print(ankur.printdetails())
print(ankur.salary)