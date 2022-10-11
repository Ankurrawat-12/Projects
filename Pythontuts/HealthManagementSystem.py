# Exercise 5: Health Management System
"""
3 clients - > Ankur , Saurabh , Ajay
Total 6 files
WAF that when executed takes as input clint name
USe this function:-
    def getdate():
        import datetime
        return datetime.datetime.now()
"""


def getdate():
    import datetime
    return datetime.datetime.now()


time_now = getdate()
timeNow = str(time_now)
print(timeNow)
repeat = True
while repeat:
    choice1 = input("Do you want to lock or retrieve :- ").lower()
    if choice1 == 'lock':
        choice12 = input("What do you want to lock :- Diet , Exercise :- ").lower()
        if choice12 == 'diet':
            choice121 = input("Whom diet do you want to lock :- Ankur , Saurabh , Ajay :- ").lower()
            if choice121 == 'ankur':
                diet = input("What do you want to lock in the diet :- ")
                f = open("ankur_diet.txt", "a")
                hell = "[" + timeNow + "]" + diet + "\n"
                f.write(hell)
                f.close()
            elif choice121 == 'saurabh':
                diet = input("What do you want to lock in the diet :- ")
                f = open("saurabh_diet.txt", "a")
                hell = "[" + timeNow + "]" + diet + "\n"
                f.write(hell)
                f.close()
            elif choice121 == 'ajay':
                diet = input("What do you want to lock in the diet :- ")
                f = open("ajay_diet.txt", "a")
                hell = "[" + timeNow + "]" + diet + "\n"
                f.write(hell)
                f.close()
            else:
                print("please chose a correct name.")
        elif choice12 == 'exercise':
            choice122 = input("Whom exercise do you want to lock :- Ankur , Saurabh , Ajay :- ").lower()
            if choice122 == 'ankur':
                exercise = input("What do you want to lock in the Exercise :- ")
                f = open("ankur_exercise.txt", "a")
                hell = "[" + timeNow + "]" + exercise + "\n"
                f.write(hell)
                f.close()
            elif choice122 == 'saurabh':
                exercise = input("What do you want to lock in the Exercise :- ")
                f = open("saurabh_exercise.txt", "a")
                hell = "[" + timeNow + "]" + exercise + "\n"
                f.write(hell)
                f.close()
            elif choice122 == 'ajay':
                exercise = input("What do you want to lock in the Exercise :- ")
                f = open("ajay_exercise.txt", "a")
                hell = "[" + timeNow + "]" + exercise + "\n"
                f.write(hell)
                f.close()
            else:
                print("please chose a correct name.")
        else:
            print("Please Enter a valid option.")
    elif choice1 == 'retrieve':
        choice13 = input("What do you want to Retrieve :- Diet , Exercise :- ").lower()
        if choice13 == 'diet':
            choice131 = input("Whom diet do you want to Retrieve :- Ankur , Saurabh , Ajay :- ").lower()
            if choice131 == 'ankur':
                f = open("ankur_diet.txt")
                print(f.read())
                f.close()
            elif choice131 == 'saurabh':
                f = open("saurabh_diet.txt")
                print(f.read())
                f.close()
            elif choice131 == 'ajay':
                f = open("ajay_diet.txt")
                print(f.read())
                f.close()
            else:
                print("please chose a correct name.")
        elif choice13 == 'exercise':
            choice132 = input("Whom exercise do you want to Retrieve :- Ankur , Saurabh , Ajay :- ").lower()
            if choice132 == 'ankur':
                f = open("ankur_exercise.txt")
                print(f.read())
                f.close()
            elif choice132 == 'saurabh':
                f = open("saurabh_exercise.txt")
                print(f.read())
                f.close()
            elif choice132 == 'ajay':
                f = open("ajay_exercise.txt")
                print(f.read())
                f.close()
            else:
                print("please chose a correct name.")
    else:
        print("Please enter a correct choice.")
    mask = input("Do you want to continue Yes or no :- ").lower()
    if mask == 'yes':
        repeat = True
    else:
        repeat = False
