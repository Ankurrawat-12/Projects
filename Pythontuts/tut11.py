# Python Exercise 1 - My Dictionary
dictionary = {"python": "https://www.w3schools.com/python/",
              "string": "https://www.w3schools.com/python/python_strings.asp",
              "list": "https://www.w3schools.com/python/python_list.asp",
              "tuples": "https://www.w3schools.com/python/python_tuples.asp",
              "dictionary": "https://www.w3schools.com/python/python_dictionaries.asp"}

print(dictionary.keys())
choice = input("Chose one :-").lower()
print(dictionary[choice])
