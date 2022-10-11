# # Exercise 7: Healthy Programmer
#
# """
# 9am - 5pm
# Water - water.mp3 (3.5 liters) - Drank(enter) - log(which timestamps)
# Eyes - eyes.mp3 - EyDone(enter) - every 30 min - log(which timestamps)
# Physical activity - physical.mp3 - ExDone(enter) - every 1hr - log(which timestamps)
#
# Rules :-
# Pygame module to play audio
# """

import time
from pygame import mixer


def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


def water_program():
    water = ''
    while water != 'drank':
        play_music(water_music)
        print("\n", end="")
        water = input("if you drank the water type (drank) :- ").lower()
        if water == 'drank':
            f = open("Healthy_programmer.txt", "a")
            wat = "[ " + str(time.asctime(time.localtime(time.time()))) + " ] Drank " + str(glass_size) + " ml Water \n"
            f.write(wat)
            f.close()
            print("Thank you !!!")
            mixer.music.stop()
            time.sleep(water_interval)
            break


def eyes_program():
    eyes = ''
    while eyes != 'eydone':
        play_music(eye_music)
        print("\n", end="")
        eyes = input("if you did the eyes exercise type (eydone) :- ").lower()
        if eyes == 'eydone':
            f = open("Healthy_programmer.txt", "a")
            eye = "[ " + str(time.asctime(time.localtime(time.time()))) + " ] Eye Exercise \n"
            f.write(eye)
            f.close()
            print("Thank you !!!")
            mixer.music.stop()
            time.sleep(eye_exercise_interval)
            break


def physical_program():
    physical = ''
    while physical != 'exdone':
        play_music(physical_music)
        print("\n", end="")
        physical = input("if you did the physical exercise type (exdone) :- ").lower()
        if physical == 'exdone':
            f = open("Healthy_programmer.txt", "a")
            phy = "[ " + str(time.asctime(time.localtime(time.time()))) + " ] Physical Exercise \n"
            f.write(phy)
            f.close()
            print("Thank you !!!")
            mixer.music.stop()
            time.sleep(physical_exercise_interval)
            break


current_time = time.strftime("%H:%M:%S")
work_start_time = '09:00:00'
work_end_time = '17:00:00'
water_limit = 3500  # in ml
glass_size = 200  # in ml
no_of_glass = round(water_limit / glass_size)
total_working_time = 8 * 60 * 60  # Assume 8 hours
water_interval = total_working_time / no_of_glass  # seconds
water_music = 'water.mp3'
eye_exercise_interval = 30 * 60  # Every 30 minutes
eye_music = 'eyes.mp3'
physical_exercise_interval = 45 * 60  # Every 45 minutes
physical_music = 'physical.mp3'

try:
    interval = 0
    glass = 0
    while current_time is not work_end_time:
        if (current_time >= work_start_time) and (current_time <= work_end_time):
            if glass == no_of_glass:
                pass
            else:
                water_program()
                glass += 1
            eyes_program()
            physical_program()
            current_time = time.strftime("%H:%M:%S")


except IndexError as er:
    print("Something wrong !!!")
