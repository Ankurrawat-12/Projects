No1 = int(input("Enter 1st number :- "))
No2 = int(input("Enter 2nd number :- "))

print("1.+\n2.-\n3.*\n4./\n")
operator = input()
if operator == '1':
    print(No1, "+", No2, "=", No1+No2)
if operator == '2':
    print(No1, "-", No2, "=", No1-No2)
if operator == '3':
    print(No1, "*", No2, "=", No1*No2)
if operator == '4':
    print(No1, "/", No2, "=", No1/No2)
else:
    print("Please enter a correct operator")
