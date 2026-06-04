from tkinter import *
import json
from utils import *

def open_reminder():
    win = Toplevel()
    win.title("Reminder")
    win.geometry("400x350")
    win.config(bg=BG_COLOR)

    card = Frame(win, bg=CARD_COLOR, padx=20, pady=20)
    card.pack(padx=20, pady=20, fill="both", expand=True)

    Label(
        card,
        text="⏰ Hydration Reminder",
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

        if current < goal:
            message = f"Drink {goal-current} more glasses today 💧"
        else:
            message = "Great Job! Goal Reached 🎉"
    except:
        message = "No data available."

    Label(
        card,
        text=message,
        font=("Arial", 16),
        bg=CARD_COLOR,
        fg=TEXT,
        wraplength=300
    ).pack(pady=40)
    
    win.lift()
    win.focus_force()