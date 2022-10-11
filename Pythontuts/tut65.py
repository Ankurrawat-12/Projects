# Super() and Overriding In Classes

class A:
    classvaar1 = "I am a class variable in calss A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvaar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvaar1 = "I am   in class B"
    def __init__(self):
        # super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvaar1 = "Instance var in class B"
        super().__init__()
        print(super().classvaar1)



a = A()
b = B()

print(b.special, b.var1, b.classvaar1)