# Decorators In Python

# def function1():
#     print("Subscribe now")
#
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executer(func):
#     func("This")
#
# executer(print)

def dec1(func1):
    def now_executing():
        print("Executing now")
        func1()
        print("Executed")
    return now_executing


@dec1
def who_is_ankur():
    print("Ankur is a good boy")


# who_is_ankur = dec1(who_is_ankur)
who_is_ankur()

"""
@dec1
def who_is_harry():
    print("Harry is a good boy")


# who_is_harry = dec1(who_is_harry)
who_is_harry()
"""
