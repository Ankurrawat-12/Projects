# Faulty Calculator

"""
Design a Calculator which will correctly solve all the problems
except the following ones :-
45*3=555,56+9=77,56/6=4
Your program should take take the operator and the two numbers
as input from the user and then return the result
"""

No1 = int(input("Enter 1st number :- "))
No2 = int(input("Enter 2nd number :- "))

print("+\t-\t*\t/\n")
operator = input()

if (No1 == 45) and (No2 == 3) and (operator == '*'):
    print(No1, " * ", No2, " = 555")
elif (No1 == 56) and (No2 == 9) and (operator == '+'):
    print(No1, " + ", No2, " = 77")
elif (No1 == 56) and (No2 == 6) and (operator == '/'):
    print(No1, " / ", No2, " = 4")
elif operator == '+':
    print(No1, " + ", No2, " = ", No1+No2)
elif operator == '-':
    print(No1, " - ", No2, " = ", No1-No2)
elif operator == '*':
    print(No1, " * ", No2, " = ", No1*No2)
elif operator == '/':
    print(No1, " / ", No2, " = ", No1/No2)
else:
    print("Please enter a correct operator")
