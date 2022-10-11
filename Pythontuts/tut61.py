# Multiple Inheritance


class Employee:
    no_of_leaves = 8
    # var = 8 2nd

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


class Player:
    no_of_games = 4
    var = 9  # 3rd

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The Name is {self.name}. Game is {self.game}"


class CoolProgrammer(Employee, Player):
    language = "C++"
    # var = 10 1st
    def print_language(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
shubham = Player("Shubham", ["Cricket"])
ankur = CoolProgrammer("Ankur", 9833, "Cool Programmer")

det = ankur.printdetails()
ankur.print_language()
print(ankur.var)
print(det)
