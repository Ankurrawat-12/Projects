# Writing And Appending To A File

# a = open("ankur2.txt", "w")
# f = a.write("Ankur is the best\n")
# print(f)
# a.close()

a = open("ankur2.txt", "r+")
print(a.read())
a.write("Thank you\n")
a.close()
