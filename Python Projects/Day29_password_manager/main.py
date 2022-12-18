from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
import json


# -----------------------------SEARCH FOR PASSWORD---------------------------------------- #
def pass_search():
    website = website_entry.get().capitalize()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="There is no password saved!")
    else:
        if website in data:
            password = data[website]['Password']
            email = data[website]['Email']
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showwarning(title='Warning!', message=f"{website} does not have a saved password!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    new_pass = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, new_pass)
    pyperclip.copy(new_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get().capitalize()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {website: {'Email': email,
                          'Password': password
                          }
                }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Warning', message="Don't leave any of the fields empty!")
    else:
        try:
            # Try reading the old data
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If there is an error, create the file by opening to write
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # If no error, update the data file with the new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Write the updated data into the data file
                json.dump(data, data_file, indent=4)
        finally:
            # No matter what happens, delete the previous entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create a window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Create a canvas
canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Create labels
# Create website label
website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)
# Create Email/Username label
user_name_label = Label(text='Email/Username:')
user_name_label.grid(column=0, row=2)
# Create Password label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Create entries
# Create website entry
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()
# Create email entry
user_name_entry = Entry(width=50)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, 'elzoremmanuel@gmail.com')
# Create password entry
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Create buttons
# Create Generate Password button
generate_button = Button(text='Generate Password', command=gen_pass)
generate_button.grid(column=2, row=3)
# Create Add button
add_button = Button(text='Add', width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
# Create Search button
search_button = Button(text='Search', width=14, command=pass_search)
search_button.grid(column=2, row=1)

window.mainloop()
