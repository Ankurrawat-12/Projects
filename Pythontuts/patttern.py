no_Of_Times = int(input("Enter the number of times you want to print the pattern :- "))

i = 0
j = 0
for i in range(0, no_Of_Times):
    for j in range(0, i+1):
        print("*", end=" ")
    print()
