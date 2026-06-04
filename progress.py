from tkinter import *
from tkinter import ttk
import json
from utils import *

def open_progress():
    win = Toplevel()
    win.title("Progress")
    win.geometry("400x400")
    win.config(bg=BG_COLOR)

    card = Frame(win, bg=CARD_COLOR, padx=20, pady=20)
    card.pack(padx=20, pady=20, fill="both", expand=True)

    Label(
        card,
        text="📈 Daily Progress",
        font=FONT_TITLE,
        bg=CARD_COLOR,
        fg=PRIMARY
    ).pack(pady=20)

    try:
        with open("users.json", "r") as file:
            user = json.load(file)

        with open("water_data.json", "r") as file:
            water = json.load(file)

        goal = user["goal"]
        current = water["glasses"]

        percent = (current / goal) * 100

        Label(
            card,
            text=f"{percent:.1f}% Completed",
            font=("Arial", 22, "bold"),
            bg=CARD_COLOR,
            fg=TEXT
        ).pack(pady=15)

        bar = ttk.Progressbar(
            card,
            orient="horizontal",
            length=250,
            mode="determinate"
        )
        bar.pack(pady=15)
        bar["value"] = percent
    except:
        Label(
            card,
            text="No data available.",
            bg=CARD_COLOR
        ).pack()

    win.lift()
    win.focus_force()