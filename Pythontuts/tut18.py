# Break & Continue Statements In Python
i = 1
"""
while True:
    if (i % 2 == 0) and (i % 5 == 0):
        i = i + 1
        continue
    print(i, end="\n")
    if i == 51:
        break  # stop the loop
    i = i + 1
"""
# Quiz
user_input = int(input("Please enter a number :- "))

while True:
    if user_input > 100:
        print("Congratulations you entered a number greater then 100")
        break
    else:
        user_input = int(input("Please Enter the number again :- "))
