# Functions And Docstrings
# a = 9
# b = 8
# c = sum((a, b))  # built in function


# def function1(a, b):
#     print("Hello You are in function1 ", a+b)


# print(function1(5, 7))
# function1(5, 7)


def function2(a, b):
    """This is a function which will calculate the average of two numbers
    This function does not work for three numbers"""
    average = (a + b)/2
    print("Hello you are in function2")
    # print(average)
    return average


print(function2.__doc__)
v = function2(5, 7)
print(v)
# print(print.__doc__)
