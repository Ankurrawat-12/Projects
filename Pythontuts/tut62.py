# Multilevel Inheritance

"""
class Dad:
    basketball = 6


class Son(Dad):
    dance = 1
    basketball = 9

    def isdance(self):
        return f"Yes i dance {self.dance} no of times"


class Grandson(Son):
    dance = 6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
               f"Yes i dance very awesomely {self.dance} no of times"


darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)
print(darry.guitare)
"""


class ElectronicDevice:
    def __init__(self,name):
        name = name
    time_taken = 15
    price = 100

    def details(self):
        return f"It takes {self.time_taken} sec and its price is {self.price}"

    @staticmethod
    def info():
        return f"It is built in 1940 "


class PocketGadgets(ElectronicDevice):
    def __init__(self,name):
        name = name
    time_taken = 10
    price = 200

    def details(self):
        return f"It takes {self.time_taken} sec and its price is {self.price}"

    @staticmethod
    def info():
        return f"It is built in 1960 "


class Phone(PocketGadgets):
    def __init__(self,name):
        name = name
    time_taken = 5
    price = 500

    def details(self):
        return f"It takes {self.time_taken} sec and its price is {self.price}"

    @staticmethod
    def info():
        return f"It is built in 1980 "


computer = ElectronicDevice("Computer")
calculator = PocketGadgets("Calculator")
mobile = Phone("Mobile")
print(computer.details())
print(computer.info())
print(calculator.details())
print(calculator.info())
print(mobile.details())
print(mobile.info())