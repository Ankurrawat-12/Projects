# Using Python External & Built In Modules

import random
# import pyperclip
# from emoji import emojize
# import wikipedia
# import turtle
# from urllib.request import urlopen
# import sys
# import antigravity


print("random")
random_number = random.randint(0, 5)
print(random_number)
rand = random.random() * 100
print(rand)
lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(lst)
print(choice)
print()

# Quiz
"""
import pyperclip
you can copy from anywhere and it will past it  
by using pyperclip.past()
and you can copy by using pyperclip.copy()
"""
print("pyperclip")
"""
print(pyperclip.paste())
pyperclip.copy("Isn't pyperclip interesting?")
past = pyperclip.paste()
print(past)
"""
print()

"""
from emoji import emojize
"""
print("emoji")
"""
print("For more emojis visit :- https://www.webfx.com/tools/emoji-cheat-sheet/")
print(emojize(":thumbs_up:"))
print(emojize(":green_heart:"))
"""
print()

"""
howdoi make trees in Python
howdoi commit in git
"""
print("use howdoi in terminal to know something")
print()

"""
import wikipedia
If you wish to get a particular number of sentences from the summary,
just pass that as an argument to the summary() function:
"""
print("wikipedia")
"""
result = wikipedia.page("Wikipedia")
print(result.summary)
print(wikipedia.summary("Debugging", sentences = 2))
"""
print()

"""
import turtle
"""
print("Turtle")
"""
my_turtle = turtle.Turtle()
myWin = turtle.Screen()


def draw_spiral(my_turtle, line_len):
    my_turtle.forward(line_len)
    my_turtle.right(90)
    draw_spiral(my_turtle, line_len - 10)


draw_spiral(my_turtle, 80)
myWin.exitonclick()
"""
print()
"""
from urllib.request import urlopen
You can also see the coding of the website by using read() function:
"""
print("from urllib.request import urlopen")
"""
page = urlopen("http://youtube.com/")
print(page.headers)
# Fetches the code
# of the web page
content = page.read()
print(content)
"""
print()
"""
You may have used the sys module before 
but did you know you could exit your program early using it?
We can cause the program to terminate by calling the sys.exit() 
function. Since this function is in the sys module, firstly, 
the sys module should be imported. This is not a third party module
and comes built-in with Python so there is no need to install it.
"""
print("import sys")
"""
while True:
    print("Type 'exit' to exit")
    response = input()
    if response == "exit":
        print("Exiting the program")
        sys.exit()
    print("You typed", response)
    if response == "no":
        break
"""
print()

"""
This opens up a page in your web browser which contains a 
comical abstract of Python developed for your delight.
Congratulations! You know have the ability to fly or for now the 
ability to visit this link https://xkcd.com/353/.
"""
print("import antigravity")
