# Python Comprehensions

# ls = []
#
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)

# ls = [i for i in range(100) if i % 3 == 0]
#
# print(ls)

# dict1 = {0: "item0", 1: "item1"}
# dict1 = {i: f"Item {i}" for i in range(1, 1001) if i % 100 == 0}
# dict1 = {i: f"Item {i}" for i in range(5)}
# dict2 = {value: key for key, value in dict1.items()}
# print(dict1,"\n", dict2)


# dresses = {dress for dress in ["dress1", "dress2", "dress3",
#                                "dress1", "dress2", "dress3"]}
#
# print(type(dresses))
# print(dresses)

# evens = (i for i in range(100) if i % 2 == 0)
# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
#
# for item in evens:
#     print(item)

_input1 = int(input("What do you want to do :- \n"
                    "1)list comprehension\n"
                    "2)Set comprehension\n"
                    "3)Dictionary comprehension\n"))

if _input1 == 1:
    _input = input("Enter a list with , separating the values :- \n")
    ls = _input.split(",")
    list1 = [items for items in ls]
    print(list1)
elif _input1 == 2:
    _input = input("Enter a list with , separating the values :- \n")
    ls = _input.split(",")
    set1 = {items for items in ls}
    print(set1)
elif _input1 == 3:
    _input = input("Enter a list with , separating the Key only :- \n")
    key = _input.split(",")
    _input2 = input("Enter a list with , separating the value only :- \n")
    value = _input2.split(",")
    dict1 = {key[i]: value[i] for i in range(len(key))}
    print(dict1)
