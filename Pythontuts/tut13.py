# If Else & Elif Conditionals In Python

# var1 = 6
# var2 = 56
# var3 = int(input())

# if var3 > var2:
#     print("Greater")
# elif var3 == var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 7, 3]
# print(15 not in list1)
# print(15 in list1)
# if 5 in list1:
#     print("Yes 5 is in the list")
# if 15 not in list1:
#     print("No 15 it's in the list")
#
# Quiz

age = int(input("Please enter your age :- "))
if (age < 18) and (age >= 7):
    print("You can't drive now")
elif (age > 18) and (age < 100):
    print("You can drive now")
else:
    print("Please visit your nearest authority ")
