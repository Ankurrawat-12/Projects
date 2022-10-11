# Exercise 6: Game Development: Snake Water Gun

"""
snake > water > gun > snake
"""

import random as ran


def player_turn():
    player = input("snake , water , gun :- ").lower()
    return player


def cpu_turn(options):
    cpu = ran.choice(options)
    return cpu


def game(c, u):
    global draw, lose, win
    if (c == 'snake') and (u == 'water'):
        print("you Lose")
        lose += 1
    elif (c == 'snake') and (u == 'gun'):
        print("you won")
        win += 1
    elif (c == 'snake') and (u == 'snake'):
        print("Draw")
        draw += 1
    elif (c == 'water') and (u == 'water'):
        print("Draw")
        draw += 1
    elif (c == 'water') and (u == 'gun'):
        print("you lose")
        lose += 1
    elif (c == 'water') and (u == 'snake'):
        print("you won")
        win += 1
    elif (c == 'gun') and (u == 'water'):
        print("you won")
        win += 1
    elif (c == 'gun') and (u == 'gun'):
        print("draw")
        draw += 1
    elif (c == 'gun') and (u == 'snake'):
        print("you Lose")
        lose += 1
    else:
        print("please chose form the given options")


def play_again():
    again = input("Do you want to play again (yes,no) :- ").lower()
    global play
    if again == "yes":
        play = True
    elif again == "no":
        print("Quitting\nFinal Results :- ")
        play = False
        print(f"Win :- {win} times \nLose :- {lose} times \nDraw :- {draw} times")
    else:
        print("please enter correctly")
        play_again()


game_options = ["snake", "water", "gun"]
play = True
draw = 0
lose = 0
win = 0
while play:
    cpu_choice = cpu_turn(game_options)
    player_choice = player_turn()
    print(f"CPU chose :- {cpu_choice}")
    print(f"You chose :- {player_choice}")
    game(cpu_choice, player_choice)
    play_again()
