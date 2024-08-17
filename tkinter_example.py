import tkinter


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

# Lable
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "normal"))
my_label["text"] = "New text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
