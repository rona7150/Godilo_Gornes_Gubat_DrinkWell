from tkinter import *
from tkinter import messagebox
import json
from utils import *

def open_register():
    win = Toplevel()
    win.title("Register")
    win.geometry(WINDOW_SIZE)
    win.config(bg=BG_COLOR)

    card = Frame(win, bg=CARD_COLOR, padx=25, pady=25)
    card.pack(padx=20, pady=30, fill="both", expand=True)

    Label(
        card,
        text="👤 User Registration",
        font=FONT_TITLE,
        bg=CARD_COLOR,
        fg=PRIMARY
    ).pack(pady=15)

    Label(card, text="Full Name", font=FONT_TEXT, bg=CARD_COLOR).pack(anchor="w")

    name_entry = Entry(card, font=("Arial", 14))
    name_entry.pack(fill="x", pady=10)

    Label(card, text="Age", font=FONT_TEXT, bg=CARD_COLOR).pack(anchor="w")

    age_entry = Entry(card, font=("Arial", 14))
    age_entry.pack(fill="x", pady=10)

    def save_user():
        try:
            name = name_entry.get()
            age = int(age_entry.get())

            if age <= 12:
                goal = 5
                group = "Kids"
            elif age <= 19:
                goal = 8
                group = "Teens"
            elif age <= 59:
                goal = 10
                group = "Adults"
            else:
                goal = 7
                group = "Elders"

            data = {
                "name": name,
                "age": age,
                "group": group,
                "goal": goal
            }

            with open("users.json", "w") as file:
                json.dump(data, file)

            messagebox.showinfo(
                "Success",
                f"Welcome {name}!\nDaily Goal: {goal} glasses"
            )
        except:
            messagebox.showerror(
                "Error",
                "Please enter valid details."
            )

    Button(
        card,
        text="Register",
        command=save_user,
        font=FONT_BUTTON,
        bg=PRIMARY,
        fg="white",
        relief="flat",
        pady=10
    ).pack(fill="x", pady=20)
    
    win.lift()
    win.focus_force()