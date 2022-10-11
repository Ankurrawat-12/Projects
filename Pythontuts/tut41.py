# *args and **kwargs In Python

def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

# def funargs(*argsankur, normal) #this will throw an error


def funargs(normal, *argsankur, **kwargsajay):
    print(type(argsankur))  # this will always change into tuple
    print(normal)
    for items in argsankur:
        print(items)
    print("\nNow i would like to introduce some of our heroes :- ")
    for key, value in kwargsajay.items():
        print(f"{key} is {value}")


# function_name_print("Ankur", "Saurabh", "Ajay", "Rohan", "Shivam")

ank = ["Ankur", "Saurabh", "Ajay", "Rohan", "Shivam"]
print(type(ank))
normal1 = "This is a normal argument and the students are :-"
kw = {"Ankur": "The Programmer", "Saurabh": "Monitor",
      "Ajay": "Fitness Instructor", "Rohan": "coordinator",
      "Shivam": "Cook"}

funargs(normal1, *ank, **kw)
# funargs(*ank, normal1) always pass the normal arguments
# before passing the *args then **kwargs
