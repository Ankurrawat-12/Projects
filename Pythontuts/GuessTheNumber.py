# Python Exercise 3 - Guess The Number

correctNumber = 73
noOfGuesses = 5

while True:
    userGuess = int(input("Enter a number :- "))
    if userGuess == correctNumber:
        print("You won and you took ", 5 - noOfGuesses, "guesses")
        break
    elif userGuess != correctNumber:
        if userGuess > correctNumber:
            print("Your guess is greater then the correct number")
        else:
            print("Your guess is Lesser then the correct number")
        noOfGuesses -= 1
        print("Number of guesses left :- ", noOfGuesses)
    if noOfGuesses == 0:
        print("Game Over you cant guess the number . The correct number is ", correctNumber)
