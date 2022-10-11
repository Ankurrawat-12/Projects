# Setters & Property Decorators

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


ankur_rawat = Employee("Ankur", "Rawat")
print(ankur_rawat.email)
ankur_rawat.fname = "Ajay"
print(ankur_rawat.email)
ankur_rawat.email = "Ankur.rawatc6rcitt@gmail.com"
print(ankur_rawat.email)
print(ankur_rawat.fname)
print(ankur_rawat.lname)
del ankur_rawat.email
print(ankur_rawat.email)
ankur_rawat.email = "Ajay.rawatc6rcitt@gmail.com"
print(ankur_rawat.email)
