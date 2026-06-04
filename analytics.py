from tkinter import *
import json
from utils import *

def open_analytics():
    win = Toplevel()
    win.title("Analytics")
    win.geometry("400x450")
    win.config(bg=BG_COLOR)

    card = Frame(win, bg=CARD_COLOR, padx=20, pady=20)
    card.pack(padx=20, pady=20, fill="both", expand=True)

    Label(
        card,
        text="📊 Analytics",
        font=FONT_TITLE,
        bg=CARD_COLOR,
        fg=PRIMARY
    ).pack(pady=20)

    try:
        with open("water_data.json", "r") as file:
            water = json.load(file)

        daily = water["glasses"]
        weekly = daily * 7
        monthly = daily * 30

        Label(
            card,
            text=f"💧 Daily Intake: {daily}",
            font=("Arial", 15),
            bg=CARD_COLOR
        ).pack(pady=10)

        Label(
            card,
            text=f"📅 Weekly Estimate: {weekly}",
            font=("Arial", 15),
            bg=CARD_COLOR
        ).pack(pady=10)

        Label(
            card,
            text=f"🗓 Monthly Estimate: {monthly}",
            font=("Arial", 15),
            bg=CARD_COLOR
        ).pack(pady=10)
    except:
        Label(
            card,
            text="No analytics available.",
            bg=CARD_COLOR
        ).pack()
    
    win.lift()
    win.focus_force()