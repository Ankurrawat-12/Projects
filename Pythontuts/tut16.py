# For Loops In Python
"""
list1 = ["Ankur", "Harry", "Saurabh", "Ajay"]
print(list1[0], list1[1])
for item in list1:
    print(item)
tuple1 = ("Ankur", "Harry", "Saurabh", "Ajay")
for item in tuple1:
    print(item)
"""
# Code
"""
list1 = [["Ankur", 1], ["Harry", 2], ["Saurabh", 3], ["Ajay", 4]]  # List of list
dict1 = dict(list1)
print(dict1)
for item, Roll in list1:
    print(item, "roll no ", Roll)

for item in dict1:
    print(item)
"""
# for item, Roll in dict1.items():
#     print(item, "roll no ", Roll)

# Quiz

items = [int, float, "Ankur", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)
