import json

from display import show, show_array
import tkinter as tk

name, surname = "", ""
i = 0
while name == "" or surname == "":
    root = tk.Tk()
    root.title("Log in")
    root.geometry("640x480")
    both = tk.IntVar()
    both.set(0)

    tk.Label(root, text="Name:").grid(row=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)
    tk.Label(root, text="*", fg="red", font="Arial 10").grid(row=0, column=2)
    tk.Label(root, text="Surname:").grid(row=1)
    surname_entry = tk.Entry(root)
    surname_entry.grid(row=1, column=1)
    tk.Label(root, text="*", fg="red", font="Arial 10").grid(row=1, column=2)
    tk.Radiobutton(root, text="Show both on one map", variable=both, value=0).place(relx=0.0, rely=0.1)
    tk.Radiobutton(root, text="Show two separate maps", variable=both, value=1).place(relx=0.3, rely=0.1)


    def submitted():
        global name, surname
        name = name_entry.get()
        surname = surname_entry.get()
        root.destroy()


    submit_button = tk.Button(root, text="Submit", command=submitted).place(relx=0.0, rely=0.15)
    if i > 0:
        tk.Label(root, text="* You must enter name and surname", font="Arial 8", fg="red").place(relx=0.0, rely=0.225)
    root.mainloop()
    i += 1

with open("objects.json", "r") as input_file:
    places = json.load(input_file)


def get_name(word):
    left = -1
    right = len(places) - 1
    while right - left > 1:
        m = (right + left) // 2
        if places[m] >= word:
            right = m
        else:
            left = m
    return places[right]


if both.get() == 1:
    show(get_name(name))
    show(get_name(surname))
else:
    show_array([get_name(name), get_name(surname)])
