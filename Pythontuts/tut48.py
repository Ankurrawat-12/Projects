# Map, Filter & Reduce

print("-------------------Map---------------------")
"""
numbers = ["3", "34", "64"]
# print(map(int, numbers))  # gives map object
numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
# print(numbers[2])


# def sq(a):
#     return a*a
#
#
# num = [2, 3, 5, 6, 76, 3, 3, 2]
# square = list(map(sq, num))
# print(square)

num = [2, 3, 5, 6, 76, 3, 3, 2]
square = list(map(lambda x:x*x , num))
print(square)
"""


"""
def single(a):
    return a


def square(a):
    return a*a


def cube(a):
    return a*a*a


def biquadratic(a):
    return a*a*a*a


func = [single, square, cube, biquadratic]
# num = [2, 3, 5, 6, 76, 3, 3, 2]
for i in range(11):
    val = list(map(lambda x:x(i), func))
    print(val)
"""

print("-------------------Filter---------------------")
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5


gr_then_5 = list(filter(is_greater_5, list_1))
# print(gr_then_5)  # gives filter object
print(gr_then_5)
"""


print("-------------------Reduce---------------------")
from functools import reduce

list1 = [1, 2, 3, 4, 59]
num = reduce(lambda x, y: x+y, list1)
# num = 0
# for i in list1:
#     num += i
# print(num)
print(num)
