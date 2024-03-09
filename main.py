from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_number

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")

    else:
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
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(110, 85, image=lock_image)
canvas.grid(row=0, column=1, pady=20, sticky="nsew")

website_label = Label(text="Website:", font=("Georgia", 8, "bold"))
website_label.grid(row=1, column=0, sticky="w")
email_label = Label(text="Email/Username:", font=("Georgia", 8, "bold"))
email_label.grid(row=2, column=0, sticky="w")
password_label = Label(text="Password:", font=("Georgia", 8, "bold"))
password_label.grid(row=3, column=0, sticky="w")

website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, pady=5, sticky="nsew", columnspan=2)
website_entry.focus()
email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, pady=5, sticky="nsew", columnspan=2)
email_entry.insert(0, "supun1018@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, pady=5)

generate_pass = Button(text="Generate Password", bg="#D0B8A8", fg="#F5F5F5", command=generate_password)
generate_pass.grid(row=3, column=2, padx=5)

add = Button(text="Add", width=44, bg="#FF6D60", fg="#F5F5F5", command=save_details)
add.grid(row=4, column=1, columnspan=2, pady=15, sticky="nsew")

window.mainloop()

print()