#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.readline()
    print(letter)

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.read()
    print(names)

name = names.split("\n")

new_name = letter.replace("[name]", name[5])

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file2:
    new_letter = file2.read()


