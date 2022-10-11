# If __name__==__main__ usage & necessity


def print_ankur(string):
    return f"This is tut46.py and print_ankur() function and this is :- {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("and the name is ", __name__)
if __name__ == '__main__': 
    print(print_ankur("This is also inside tut 46.py"))
    o = add(4, 6)
    print(o)
