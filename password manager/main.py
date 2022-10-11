from tkinter import *
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    password = str(password_entry.get())
    email_username = str(email_username_entry.get())
    website_app = str(website_app_entry.get())
    new_data = {
        website_app: {
            "email": email_username,
            "password": password
        }
    }

    if len(website_app) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_app, message=f"These are the details entered : "
                                                                  f"\nEmail: {email_username}\n"
                                                                  f"Password: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_app_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_data = str(website_app_entry.get())
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if search_data in data:
            email_username = data[search_data]['email']
            password = data[search_data]['password']
            messagebox.showinfo(title=search_data, message=f"Email/Username: {email_username}\n"
                                                           f"Password: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_data} exists.")

# ---------------------------- UI SETUP ------------------------------- #

# Window


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Label
website_app_label = Label(text="Website/App :-")
website_app_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username :-")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password :-")
password_label.grid(column=0, row=3)

# Entry
website_app_entry = Entry()
website_app_entry.focus()
website_app_entry.grid(column=1, row=1, sticky="EW")

email_username_entry = Entry()
email_username_entry.insert(0, "ankurrawat620@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
