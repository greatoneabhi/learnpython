from tkinter import END, Tk, Label, Entry, Button


def convert():
    miles = float(input.get())
    km = miles * 1.609
    output_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=10)

input = Entry(width=10)
input.insert(END, string="0")
input.focus()
input.grid(column=1, row=0)

miles_unit_label = Label(text="Miles")
miles_unit_label.grid(column=2, row=0)

is_equal_to_lable = Label(text="is equal to")
is_equal_to_lable.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_unit_label = Label(text="Km")
km_unit_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
