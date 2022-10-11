# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#         function()
#
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("hello")
#
#
# @delay_decorator
# def say_by():
#     print("by")
#
#
# def say_greeting():
#     print("How are you")
#
#
# say_hello()


# current_time = time.time()
# print(current_time)
#
#
# def speed_calc_decorator(function):
#     def function_wrapper():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed = {end_time - start_time}s")
#     return function_wrapper
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()

# def login_decorator(function):
#     def wrapper(*args, **kwargs):
#         print(f"you called {function.__name__}{args}")
#         result = function(args[0], args[1], args[2])
#         print(f"it returned: {result}")
#     return wrapper
#
#
# @login_decorator
# def multiplication(a, b, c):
#     return a * b * c
#
#
# multiplication(1, 2, 3)

from flask import Flask
from random import randint

GUESSED_NUMBER = randint(0, 9)
print(GUESSED_NUMBER)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=40% >'


@app.route('/<int:number>')
def guess(number):
    if number == GUESSED_NUMBER:
        return '<h1 style="color:green;text-align:center">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number < GUESSED_NUMBER:
        return '<h1 style="color:red;text-align:center">Too low,try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=40%>'
    else:
        return '<h1 style="color:violet;text-align:center">Too high,try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=40%>'


def make_bold(function):
    def function_wrapper(*args, **kwargs):
        return f"<strong>{function()}</strong>"
    return function_wrapper


def make_emphasis(function):
    def function_wrapper(*args, **kwargs):
        return f"<em>{function()}</em>"

    return function_wrapper


def make_underlined(function):
    def function_wrapper(*args, **kwargs):
        return f"<u>{function()}</u>"

    return function_wrapper


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    # return "<u><em><strong>bye</strong></em></u>"
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, your are {number} year old"


if __name__ == "__main__":
    app.run(debug=True)

