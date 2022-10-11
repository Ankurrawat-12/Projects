from csv import *
from tkinter import *
from datetime import date
from tkinter import messagebox

import cv2
from cv2 import VideoCapture, imwrite


# variables
# column space
cs = 2
date = date.today()
bg = "light blue"
font = ('Helvatical bold', 10)
isempty = True
# list
variables = ["bath", "study", "coding", "exercise", "anime", "movie", "game", "mb"]
variables2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
field_names = ["Date", "Bath", "Study", "Code", "Exercise", "Anime", "Movie", "Game", "MB", "Summary"]


# Creating window
window = Tk()
window.title("Daily Routine")
window.config(padx=10, pady=10, bg=bg)
# window.geometry("750x550")


# functions
def submit():
    for i in range(0, 8):
        # print(variables2[i].get())
        if len(variables2[i].get()) == 0:
            isempty = True
        else:
            isempty = False
    if isempty:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty or "
                                                  "haven't filled anything wrong.")
    else:
        is_ok = messagebox.askokcancel(title=date, message=f"These are the details entered :\n\n"
                                                           f"Date : {date}\n\n"
                                                           f"Bath : {variables2[0].get()}\n\n"
                                                           f"Study : {variables2[1].get()}\n\n"
                                                           f"Code : {variables2[2].get()}\n\n"
                                                           f"Exercise : {variables2[3].get()}\n\n"
                                                           f"Anime : {variables2[4].get()}\n\n"
                                                           f"Movie : {variables2[5].get()}\n\n"
                                                           f"Game : {variables2[6].get()}\n\n"
                                                           f"MB : {variables2[7].get()}\n\n"
                                                           f"Summary : {summary.get(1.0, END)}\n\nIs it ok to save?")
        # print(summary.get(1.0, END))
        if is_ok:
            data = {
                "Date": date,
                "Bath": variables2[0].get(),
                "Study": variables2[1].get(),
                "Code": variables2[2].get(),
                "Exercise": variables2[3].get(),
                "Anime": variables2[4].get(),
                "Movie": variables2[5].get(),
                "Game": variables2[6].get(),
                "MB": variables2[7].get(),
                "Summary": summary.get(1.0, END)
            }
            with open("Data/Daily_routine.csv", "a") as record:
                dictwriter_object = DictWriter(record, fieldnames=field_names)
                dictwriter_object.writerow(data)



def camera():
    cam_port = 0
    cam = VideoCapture(cam_port, cv2.CAP_DSHOW)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

        # showing result, it take frame name and image
        # output
        # imshow(f"{date}", image)

        # saving image in local storage
        imwrite(f"img/{date}.png", image)

        # If keyboard interrupt occurs, destroy image
        # window
        # waitKey(0)
        # destroyWindow(f"{date}")
        cam.release()

        # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
    cv2.destroyAllWindows()


# labels
heading = Label(text="Daily Routine", font=('Helvatical bold', 20), background=bg)
heading.grid(column=0, row=0, columnspan=2)

bath = Label(text="How many times did you Bath today?", font=font, background=bg)
bath.grid(column=0, row=1, columnspan=cs)

study = Label(text="How many Hours did you Study today?", font=font, background=bg)
study.grid(column=0, row=2, columnspan=cs)

coding = Label(text="How many Hours did you code today?", font=font, background=bg)
coding.grid(column=0, row=3, columnspan=cs)

exercise = Label(text="How many hours did you Exercise today?", font=font, background=bg)
exercise.grid(column=0, row=4, columnspan=cs)

anime = Label(text="How many Anime episodes did you watch today?", font=font, background=bg)
anime.grid(column=0, row=5, columnspan=cs)

movie = Label(text="how many Movies Did you watch today?", font=font, background=bg)
movie.grid(column=0, row=6, columnspan=cs)

game = Label(text="how many hours did you play Games today?", font=font, background=bg)
game.grid(column=0, row=7, columnspan=cs)

mb = Label(text="Secret today?", font=font, background=bg)
mb.grid(column=0, row=8, columnspan=cs)


# creating radio buttons
# for i in range(1, 7):
#     for j in range(2, 4):
#         if j == 2:
#             b1 = Radiobutton(variable=variables[i-1], text="yes", value=1, activebackground=bg,
#                              background=bg)
#         elif j == 3:
#             b1 = Radiobutton(variable=variables[i - 1], text="no", value=0, activebackground=bg,
#                              background=bg)
#         b1.grid(column=j, row=i)

# creating entry
for i in range(1, 9):
    # print(variables2[i-1])
    variables2[i-1] = Entry(background=bg, width=10)
    variables2[i-1].grid(column=2, row=i, sticky=EW)

summary = Text(width=50, height=2, background=bg)
summary.insert('end', "Summary of the day")
summary.grid(column=0, row=9, columnspan=3)

# create button
photo = Button(text="Capture", command=camera, activebackground=bg, background=bg)
photo.grid(column=1, row=10, sticky=EW)
submit = Button(text="Submit", command=submit, activebackground=bg, background=bg)
submit.grid(column=1, row=11, sticky=EW)
camera()
window.mainloop()

