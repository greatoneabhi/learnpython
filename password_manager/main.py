from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
import password_helper
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = password_helper.generate()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if validate(website=website, username=username, password=password):
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {username} "
            f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open(file="./password_manager/data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def validate(website, username, password):
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
        return False
    return True

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./password_manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# email / username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "abhishek.dumca@gmail.com")

# password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

generate_password_btn = Button(text="Generate Password", width=13, command=generate_password)
generate_password_btn.grid(row=3, column=2)

# add button
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
