import random
from tkinter import *
from PIL import Image, ImageTk
import string
import os
import pandas

window = Tk()
window.title("Image Display")
window.geometry("700x500")

canvas = Canvas(window, width=200, height=224)
canvas.grid(column=1, row=0)
img = Image.open("logo.png")
logo_img = ImageTk.PhotoImage(img)
canvas.create_image(100, 112, image=logo_img)


def generate():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def add():
    data = {
        "Website": [website_entry.get()],
        "Email": [email_username_entry.get()],
        "Password": [password_entry.get()]
    }

    if os.path.exists("all_data.csv"):
        existing_data = pandas.read_csv("all_data.csv")
        new_data = pandas.DataFrame(data)
        updated_data = existing_data.append(new_data, ignore_index=True)
    else:
        updated_data = pandas.DataFrame(data)
    updated_data.to_csv("all_data.csv", index=False)


website = Label(text="Website:")
website.grid(column=0, row=1)
website.config(padx=20, pady=20, font=("Arial", 12))
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
email_username.config(padx=20, pady=20, font=("Arial", 12))
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=20, pady=20, font=("Arial", 12))

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1)
email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=2)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", width=30, command=add)
add_button.grid(column=1, row=4)
generate_password_button = Button(text="Generate Password", width=30, command=generate)
generate_password_button.grid(column=2, row=3)

window.mainloop()

