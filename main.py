from tkinter import *
from register_user import open_register
from water_tracker import open_tracker
from reminder import open_reminder
from progress import open_progress
from analytics import open_analytics
from utils import *

root = Tk()
root.title("DrinkWell")
root.geometry(WINDOW_SIZE)
root.config(bg=BG_COLOR)
root.resizable(True, True)

# ================= HEADER =================

header = Frame(root, bg=PRIMARY, height=180)
header.pack(fill="x")

Label(
    header,
    text="💧 DrinkWell",
    font=("Arial", 28, "bold"),
    bg=PRIMARY,
    fg="white"
).pack(pady=(30, 5))

Label(
    header,
    text="Smart Hydration Tracker",
    font=("Arial", 13),
    bg=PRIMARY,
    fg="white"
).pack()

# ================= MAIN CARD =================

card = Frame(
    root,
    bg=CARD_COLOR,
    padx=20,
    pady=20
)
card.pack(padx=20, pady=20, fill="both", expand=True)

Label(
    card,
    text="Dashboard",
    font=("Arial", 20, "bold"),
    bg=CARD_COLOR,
    fg=TEXT
).pack(pady=10)

# ================= BUTTON FUNCTION =================

def create_button(text, command, color):
    Button(
        card,
        text=text,
        command=command,
        font=FONT_BUTTON,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        relief="flat",
        padx=10,
        pady=12,
        cursor="hand2"
    ).pack(fill="x", pady=8)

# ================= BUTTONS =================

create_button("👤 Register User", open_register, "#42A5F5")
create_button("🥤 Water Tracker", open_tracker, "#1E88E5")
create_button("⏰ Hydration Reminder", open_reminder, "#1976D2")
create_button("📈 Progress", open_progress, "#1565C0")
create_button("📊 Analytics", open_analytics, "#0D47A1")

Button(
    root,
    text="Exit",
    command=root.destroy,
    font=FONT_BUTTON,
    bg="#EF5350",
    fg="white",
    relief="flat",
    padx=10,
    pady=10
).pack(pady=10)

root.mainloop()