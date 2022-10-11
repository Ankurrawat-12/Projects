# Scope, Global Variables and Global Keyword
"""
l = 10  # Global variable


def function1(n):
    # l = 5  # Local variable
    m = 8
    global l
    l += 45
    print(l, m)
    print(n, "I am inside function1 ")


function1("This is Me")
print(l)
"""
x = 89


def ankur():
    x = 20

    def ajay():
        global x
        x = 88

    print("Before calling ajay() ", x)
    ajay()
    print("After calling ajay() ", x)


ankur()
print(x)

# Quiz
