from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data = f'{website} | {email} | {password}'

    if website.strip() != '' and email.strip() != '' and password.strip() != '':
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?')
        if is_ok:
            with open ('saved_data.txt','a') as file:
                file.write(f'{data}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title='Oops', message='Please don\'t leave any field empty.')
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username: ')
email_label.grid(row=2, column=0)

password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'nikki@gmail.com')

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Buttons
generate_password = Button(text='Generate Password', command=generate_password)
generate_password.grid(row=3, column=2)

add_button = Button(text='Add', width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()