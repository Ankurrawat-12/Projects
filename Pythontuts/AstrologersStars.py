# Python Exercise 4: Astrologer's Stars

no_Of_Times = int(input("Enter the number of times you want to print the pattern :- "))
typ = int(input("Enter 0 or 1 :- "))
ty = bool(typ)
if typ:
    for i in range(1, no_Of_Times+1):
        for j in range(i, i+1):
            print("*", end="")
        print()

else:
    for i in range(no_Of_Times, 0, -1):
        for j in range(1, i + 1):
            print("-", end="")
        print()
