from tkinter import *
from tkinter import ttk
import json
import os
from utils import *

def open_tracker():
    win = Toplevel()
    win.title("Water Tracker")
    win.geometry(WINDOW_SIZE)
    win.config(bg=BG_COLOR)

    glasses = IntVar(value=0)
    goal = 10

    # LOAD DATA
    if os.path.exists("water_data.json"):
        try:
            with open("water_data.json", "r") as file:
                data = json.load(file)
                glasses.set(data.get("glasses", 0))
        except:
            glasses.set(0)

    # LOAD USER GOAL
    if os.path.exists("users.json"):
        try:
            with open("users.json", "r") as file:
                user = json.load(file)
                goal = user.get("goal", 10)
        except:
            goal = 10

    card = Frame(win, bg=CARD_COLOR, padx=25, pady=25)
    card.pack(padx=20, pady=20, fill="both", expand=True)

    Label(
        card,
        text="💧 Water Intake",
        font=FONT_TITLE,
        bg=CARD_COLOR,
        fg=PRIMARY
    ).pack(pady=15)

    water_label = Label(
        card,
        text=f"{glasses.get()} / {goal} Glasses",
        font=("Arial", 26, "bold"),
        bg=CARD_COLOR,
        fg=TEXT
    )
    water_label.pack(pady=15)

    progress = ttk.Progressbar(
        card,
        orient="horizontal",
        length=300,
        mode="determinate"
    )
    progress.pack(pady=15)

    def update_ui():
        percent = (glasses.get() / goal) * 100
        progress["value"] = percent
        water_label.config(text=f"{glasses.get()} / {goal} Glasses")

    update_ui()

    def add_water():
        glasses.set(glasses.get() + 1)
        with open("water_data.json", "w") as file:
            json.dump({"glasses": glasses.get()}, file)
        update_ui()

    Button(
        card,
        text="➕ Drink Water",
        command=add_water,
        font=FONT_BUTTON,
        bg=PRIMARY,
        fg="white",
        relief="flat",
        pady=12
    ).pack(fill="x", pady=20)
    
    win.lift()
    win.focus_force()