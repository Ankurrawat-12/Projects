# Instance & Class Variables

class Employee:
    no_of_leaves = 8
    pass


harry = Employee()
ankur = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

ankur.name = "Ankur"
ankur.salary = 4554
ankur.role = "Head Programmer"
# print(harry.no_of_leaves)
# print(ankur.no_of_leaves)
print(Employee.no_of_leaves)
# harry.no_of_leaves = 9
print(harry.__dict__)
print(ankur.__dict__)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
# print(Employee.no_of_leaves)
print(Employee.no_of_leaves)
