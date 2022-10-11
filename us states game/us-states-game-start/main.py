import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen.addshape(image)
data = pandas.read_csv("50_states.csv")


def locate_state():
    cod_dict = dict(data[data.state == answer])
    x = list(cod_dict['x'])[0]
    y = list(cod_dict['y'])[0]
    tim.goto(x=x, y=y)
    tim.write(answer, move=False, align="center")


# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()


turtle.shape(image)
guessed_state = 0
all_states = data.state.to_list()
guessed_states = []
game = True
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{guessed_state}/50 States Correct", prompt="What's another state name?").title()
    if answer == "Exit":
        # missing_states = [state for state in all_states if state not in guessed_states]
        break
    if answer in all_states:
        all_states.remove(answer)
        guessed_states.append(answer)
        locate_state()
        guessed_state += 1


df = pandas.DataFrame(all_states)
df.to_csv("missing_states.csv")
