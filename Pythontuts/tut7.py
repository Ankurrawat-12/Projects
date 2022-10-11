# Variables, Data types and Typecasting | Python Tutorials For Absolute Beginners In Hindi #7
var1 = "Hello World"
var2 = 4
var3 = 36.7
var4 = "Ankur"
var5 = "34"
var6 = "35"
# print(type(var1))
# print(var2)
# print(var3)
# print(var2 + var3)
# print(var1 + var4)

'''
float()
str()
int()
'''
print(100 * int(var5) + int(var6))
print(10 * str(int(var5) + int(var6)))
# print(var5 + var6)
print(10 * "Hello World\n")

# print("Enter a number")
# input_Num = int(input())
# print("you entered a number +10", input_Num + 10)

# Quiz :- Make a calculator
number_1 = int(input("Enter 1st number :- "))
number_2 = int(input("Enter 2nd number :- "))
number_3 = number_1 + number_2
print(f"The addition of {number_1} and {number_2} is {number_3} ")
