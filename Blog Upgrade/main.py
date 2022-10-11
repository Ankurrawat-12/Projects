from flask import Flask, render_template, request
import smtplib
import requests

OWN_EMAIL2 = 'ankurrawat620@gmail.com'
OWN_EMAIL = 'ankurrawatc6rcitt@gmail.com'
OWN_PASSWORD = "b(O3eTdsH8##g"
app = Flask(__name__)

api = "https://api.npoint.io/b1b09a2fda3861f9bc9c"
data = requests.get(api).json()


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        personal_data = request.form
        send_email(personal_data["Name"], personal_data["Email"], personal_data["PhoneNumber"], personal_data["Message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL2, email_message)
    response(name, email, message)


def response(name, email, message):
    email_message = f"Subject:Thanks For Contacting Us\n\n{name},\n\tThanks for Contacting we will reply you after" \
                    f" 3 or 4 Business days regarding  your message :- '{message}'"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, email, email_message)

if __name__ == "__main__":
    app.run(debug=True, port=6969)
