"""
import colorgram

color_palette = []
revised_color_palette = []


def generate_color_palette(quantity):
    # grab the colors from an rgb image
    colors = colorgram.extract('image.jpg', quantity)

    # create empty list
    rgb_colors = []

    # for each color in colors, grab the rgb values, save as a tuple, and append to rgb_colors
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)

        rgb_colors.append(new_color)
    return (rgb_colors)


numb_of_colors = int(input("How many colors in the color palette? "))

color_palette = generate_color_palette(numb_of_colors)

# from initial colors generated
# remove swatches out of range (735 or higher)
for swatch in color_palette:
    color_strength = swatch[0] + swatch[1] + swatch[2]
    if color_strength < 735:
        revised_color_palette.append(swatch)

# here is the revised color palette. copy and paste into main.py
print(revised_color_palette)
"""
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
#
# for color in colors:
#     r = color.rgb.b
#     g = color.rgb.b
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# screen.exitonclick()
import turtle
import random

tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("fastest")
tim.hideturtle()
turtle.colormode(255)
tim.penup()
# tim.pendown()


def draw_dots():
    y = -225
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
                  (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
                  (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
                  (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
                  (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    for i in range(10):
        tim.goto(-225, y)
        y += 50
        for j in range(10):
            color = random.choice(color_list)
            tim.dot(20, tuple(color))
            tim.forward(50)


draw_dots()
screen.exitonclick()

"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
"""
