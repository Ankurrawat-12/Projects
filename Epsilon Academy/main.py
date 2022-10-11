from tkinter import *
# from tkinter.ttk import *
from csv import DictWriter
from student import Student
import pandas
from tkinter import messagebox
n = 0
BG = "#A8D1DF"
NBG = "#D8BFD8"
primary_data = {}
field_names = ["ID", "Name", "Fathers Name", "Mothers Name", "Class", "Stream", "Phone Number", "Age", "Joining Month",
               "Fees"]
months_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
               "October", "november", "December"]
data = pandas.read_csv("Data/Report.csv").to_dict(orient="records")


def open_new_window():
    i_d = search_entry.get()
    df = pandas.read_csv("Data/Report.csv")
    data = df.to_dict(orient="records")
    for v in range(len(data)):
        if int(i_d) == int(data[v]["ID"]):
            student_name = data[v]["Name"]
            fathers_name = data[v]["Fathers Name"]
            mothers_name = data[v]["Mothers Name"]
            claa_s = data[v]["Class"]
            stream = data[v]["Stream"]
            phone_number = data[v]["Phone Number"]
            age = data[v]["Age"]
            joining_month = data[v]["Joining Month"]
            fees = data[v]["Fees"]

            new_window = Toplevel(window)
            new_window.title(student_name)
            # new_window.minsize(height=500, width=500)
            new_window.config(padx=20, pady=20, bg=NBG)

            Label(new_window, text="Student Name :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=0)
            Label(new_window, text=student_name, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=0)
            Label(new_window, text="Father's Name :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=1)
            Label(new_window, text=fathers_name, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=1)
            Label(new_window, text="Mother's Name :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=2)
            Label(new_window, text=mothers_name, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=2)
            Label(new_window, text="Class :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=3)
            Label(new_window, text=claa_s, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=3)
            Label(new_window, text="Stream :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=4)
            Label(new_window, text=stream, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=4)
            Label(new_window, text="Phone Number :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=5)
            Label(new_window, text=phone_number, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=5)
            Label(new_window, text="Age :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=6)
            Label(new_window, text=age, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=6)
            Label(new_window, text="Joining Month:-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=7)
            Label(new_window, text=joining_month, bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=7)
            Label(new_window, text="Fees :-", bg=NBG, font=("ariel", 12, "italic")).grid(column=0, row=8)
            Label(new_window, text=f"₹{fees}", bg=NBG, font=("ariel", 12, "italic")).grid(column=1, row=8)
        else:
            messagebox.showinfo(title="Error!", message="No Student with this ID")
            return 0


def add_data():
    global n, primary_data
    name = str(student_name_entry.get())
    fathers_name = str(student_fathers_name_entry.get())
    mothers_name = str(student_mothers_name_entry.get())
    age = student_age_entry.get()
    phone_number = student_Phone_number_entry.get()
    clas_s = student_class_entry.get()
    identity = int(student_special_id_entry.get())
    stream = str(student_stream_entry.get())
    fees = student_fees_entry.get()
    joining_month = student_Joining_month_entry.get()
    if len(name) == 0 or len(fathers_name) == 0 or len(str(phone_number)) != 10 or len(str(fees)) == 0 or\
            len(str(joining_month)) == 0 or len(str(identity)) == 0 or int(clas_s) > 13 or len(str(age)) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty or "
                                                  "haven't filled anything wrong.")
    else:
        is_ok = messagebox.askokcancel(title=name, message=f"These are the details entered :\n\n"
                                                           f"Fathers name: {fathers_name}\n\n"
                                                           f"Mothers name: {mothers_name}\n\n"
                                                           f"Age: {age}\n\n"
                                                           f"Phone Number: {phone_number}\n\n"
                                                           f"Fees: {fees}\n\n"
                                                           f"class: {clas_s}\n\n"
                                                           f"Stream: {stream}\n\n"
                                                           f"Joining Month: {joining_month}\n\nIs it ok to save?")
        if is_ok:
            stud = Student(name=name, fathers_name=fathers_name, age=age, phone_no=phone_number, clas_s=clas_s,
                           i_d=identity,
                           mothers_name=mothers_name, stream=stream, joining_month=joining_month, fees=fees)
            primary_data = stud.make_primary_list()
            with open("Data/Report.csv", "a") as record:
                dictwriter_object = DictWriter(record, fieldnames=field_names)
                dictwriter_object.writerow(primary_data)
                student_stream_entry.delete(0, END)
                student_name_entry.delete(0, END)
                student_mothers_name_entry.delete(0, END)
                student_fathers_name_entry.delete(0, END)
                student_Phone_number_entry.delete(0, END)
                student_age_entry.delete(0, END)
                student_class_entry.delete(0, END)
                student_special_id_entry.delete(0, END)
                student_Joining_month_entry.delete(0, END)
                student_fees_entry.delete(0, END)
            data = pandas.read_csv("Data/Report.csv").to_dict(orient="records")
            student_special_id_entry.insert(0, 1000+len(data))
        # df = pandas.DataFrame(primary_data, index=[n])
        # df.to_csv("Data/Report.csv")
        # print(df)


# ---------------------------------------------- UI --------------------------------------------------------

window = Tk()
window.minsize(height=500, width=500)
window.title("Records")
window.config(padx=15, pady=15, bg=BG)

canvas = Canvas(height=84, width=84, bg=BG, highlightthickness=0)
logo = PhotoImage(file="images/Epsilon_logo1.png")
logo_canvas = canvas.create_image(42, 42, image=logo)
canvas.grid(column=0, row=0, ipady=20)

title_label = Label(text="Epsilon Academy Student Records", font=("ariel", 20, "bold"), bg=BG)
title_label.grid(column=1, row=0, columnspan=3)

student_name_label = Label(text="Student's Name ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=0, row=2, pady=10)
student_name_entry = Entry()
student_name_entry.focus()
student_name_entry.grid(column=1, row=2, sticky="ew", pady=10)


student_age_label = Label(text="Age ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=2, row=2, pady=10)
student_age_entry = Entry()
student_age_entry.grid(column=3, row=2, sticky="ew", pady=10)


student_fathers_name_label = Label(text="Father's Name ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=0, row=3, pady=10)
student_fathers_name_entry = Entry()
student_fathers_name_entry.grid(column=1, row=3, sticky="ew", pady=10)


student_mothers_name_label = Label(text="Mother's Name ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=2, row=3, pady=10)
student_mothers_name_entry = Entry()
student_mothers_name_entry.grid(column=3, row=3, sticky="ew", pady=10)


student_class_label = Label(text="Class ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=0, row=6, pady=10)
student_class_entry = Entry()
student_class_entry.grid(column=1, row=6, sticky="ew", pady=10)


student_stream_label = Label(text="Stream ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=2, row=6, pady=10)
student_stream_entry = Entry()
student_stream_entry.grid(column=3, row=6, sticky="ew", pady=10)


student_Phone_number_label = Label(text="Phone Number ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=0, row=7, pady=10)
student_Phone_number_entry = Entry()
student_Phone_number_entry.grid(column=1, row=7, sticky="ew", pady=10)


student_fees_label = Label(text="Fees ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=2, row=7, pady=10)
student_fees_entry = Entry()
student_fees_entry.grid(column=3, row=7, sticky="ew", pady=10)


student_joining_month_label = Label(text="Joining Month ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=0, row=8, pady=10)
student_Joining_month_entry = Entry()
student_Joining_month_entry.grid(column=1, row=8, sticky="ew", pady=10)


student_special_id_label = Label(text="Special ID ", font=("ariel", 12, "italic"), bg=BG)\
    .grid(column=2, row=8, pady=10)
student_special_id_entry = Entry()
student_special_id_entry.insert(0, 1000+len(data))
student_special_id_entry.grid(column=3, row=8, sticky="ew", pady=10)


add_data_button = Button(text="Add Data to Record", font=("ariel", 16, "bold"),
                         bg=BG, highlightthickness=0, bd=1, command=add_data)
add_data_button.grid(column=1, row=10, pady=20, columnspan=2, sticky="ew")

search_entry = Entry()
search_entry.grid(column=1, row=12)

search_records_button = Button(text="Search Record", font=("ariel", 16, "bold"), bg=BG, highlightthickness=0, bd=1,
                               command=open_new_window)
search_records_button.grid(column=2, row=12, pady=10, padx=10)


window.mainloop()
