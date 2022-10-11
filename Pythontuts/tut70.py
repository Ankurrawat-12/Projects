# Object Introspection
import inspect


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname},{lname}@codewithharry.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if (self.fname == None) or (self.lname == None):
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("skill", "f")


# print(skillf.email)
# print(type(skillf))
# print(type("This is a string"))
print(id("This is a string"))
# print(id("That That"))
# o = "This is a string"
# print(dir(o))
print(dir(skillf))


print(inspect.getmembers(skillf))

# Challenge
# import inspect
#
#
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#
# ankur = Employee("Ankur","Rawat")
# def insp(emp):
#      inspect.isclass(emp)
#      while True:
#        print(dir(emp))
#        break
# emp=input()
# insp(emp)
