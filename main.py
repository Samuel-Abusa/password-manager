import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from password_generator import Generator


def find_password():
    site_name = website_entry.get()

    try:
        with open("./data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops!", message="You haven't saved any password yet."
        )
    else:
        try:
            site = data[site_name]
        except KeyError:
            messagebox.showinfo(title="Oops!", message="Site not found")
        else:
            messagebox.showinfo(
                title=f"{site_name}",
                message=f"Email/Username: {site['email/username']}\nPassword: {site['password']}",
            )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
generator = Generator()


def display_password():
    password = generator.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_file(data):
    with open("./data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)


def save_password():
    entries = [website_entry, user_email_entry, password_entry]

    if 0 in [len(entry.get()) for entry in entries]:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty"
        )
    elif messagebox.askokcancel(
        title="Save Password?",
        message=f"Website: {entries[0].get()}\nEmail/Username: {entries[1].get()}\nPassword: {entries[2].get()}",
    ):
        new_data = {
            entries[0].get(): {
                "email/username": entries[1].get(),
                "password": entries[2].get(),
            }
        }

        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            update_file(new_data)
        else:
            data.update(new_data)
            update_file(data)
        finally:
            for entry in entries:
                entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_title = Label(text="Website:")
website_title.grid(row=1, column=0)
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_btn = Button(text="Search", width=13, command=find_password)
search_btn.grid(row=1, column=2)

user_email_title = Label(text="Email/Username:")
user_email_title.grid(row=2, column=0)
user_email_entry = Entry(width=50)
user_email_entry.grid(row=2, column=1, pady=10, columnspan=2)

password_title = Label(text="Password:")
password_title.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_btn = Button(text="Generate Password", command=display_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=43, command=save_password)
add_btn.grid(row=4, column=1, pady=10, columnspan=2)

window.mainloop()
