# Try Except Exception Handling In Python
print("Enter num 1")
num1 = input()
print("Enter num 1")
num2 = input()
try:
    print("The sum of these two numbers is ",
          int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")

try:
    print(Ankur)
except Exception as e:
    print(e)
for i in range(0, 10):
    print("Ankur", end=" ")
    i +=1