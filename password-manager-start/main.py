from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)



# function for saving passwords

def add_password():
    website = websites_box.get()
    email = login_box.get()
    password = pass_entry.get()
    print(f'{website}, {email}, {password}')
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    print(new_data)
    if len(pass_entry.get()) == 0 or len(websites_box.get()) == 0:
        messagebox.showinfo(title='oops', message='make sure you have not left any fields open')
    else:
        with open("passwordGenerator.txt", 'a') as filename:
            filename.write(f'{new_data}')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=70, pady=70)
canvas = Canvas(width=300, height=300)

lock_img = PhotoImage(file="logo2.png")
canvas.create_image(150, 150, image=lock_img)
canvas.grid(row=0, column=1)

websites = Label(text="Website:")
websites.grid(row=1, column=0)
websites_box = Entry(width=35)
websites_box.grid(row=1, column=1)
websites_box.focus()

login = Label(text="Email/Username:")
login.grid(row=2, column=0)
login_box = Entry(width=35)
login_box.grid(row=2, column=1)
login_box.insert(END, "JLGARDNER688@GMAIL.COM")

password = Label(text="Password:")
password.grid(row=3, column=0)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search = Button(text="Search")
search.grid(row=1, column=2)
search.config(width=20)

add = Button(text='Add', command=add_password)
add.grid(row=3, column=2, columnspan=2)
add.config(width=20)

generate_password = Button(text="Generate Password", command=make_password)
generate_password.grid(row=2, column=2)
generate_password.config(width=20)

window.mainloop()
