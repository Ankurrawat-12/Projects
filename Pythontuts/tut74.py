# Using Else With For Loops

khana = ["Roti", "Sabji", "Chawal"]

# for item in khana:
#     print(item)
#     # break
#
# else:
#     print("This for loop ended properly")

for item in khana:
    if item == "Paratha":
        print("Paratha is available in the khana list")
        break

else:
    print("Your item was not found")
