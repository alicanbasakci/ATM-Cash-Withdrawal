from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

class BankAccount:
    def __init__(self, starting_balance=13750):
        self.balance = starting_balance

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                raise ValueError("The withdrawal amount is greater than your balance!")
            self.balance -= amount
            return self.balance
        except ValueError as e:
            messagebox.showerror("Error", e)
            return None

account = BankAccount()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alica\OneDrive\Masaüstü\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def withdraw_amount():
    amount = entry.get()
    new_balance = account.withdraw(amount)
    if new_balance is not None:
        canvas.itemconfig(balance_text, text=f"Balance: {new_balance}")

def deduct_balance(amount):
    new_balance = account.withdraw(amount)
    if new_balance is not None:
        canvas.itemconfig(balance_text, text=f"Balance: {new_balance}")

window = Tk()
window.geometry("794x613")
window.configure(bg="#8CDCEC")

canvas = Canvas(
    window,
    bg="#8CDCEC",
    height=613,
    width=794,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    397.0,
    306.0,
    image=image_image_1
)

balance_text = canvas.create_text(
    311.0,
    170.0,
    anchor="nw",
    text=f"Balance: {account.balance}",
    fill="#FFFFFF",
    font=("Inter Black", 18 * -1)
)

canvas.create_text(
    580.0,
    301.0,
    anchor="nw",
    text="Other :",
    fill="#FFFFFF",
    font=("Inter Black", 14 * -1)
)

canvas.create_text(
    274.0,
    95.0,
    anchor="nw",
    text="Nicosia - Near East University ",
    fill="#FFFFFF",
    font=("Inter Black", 18 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: deduct_balance(50),
    relief="flat"
)
button_1.place(x=24.0, y=128.0, width=121.0, height=42.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: deduct_balance(500),
    relief="flat"
)
button_2.place(x=642.0, y=209.0, width=128.0, height=42.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: deduct_balance(100),
    relief="flat"
)
button_3.place(x=642.0, y=128.0, width=128.0, height=42.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: deduct_balance(1000),
    relief="flat"
)
button_4.place(x=24.0, y=290.0, width=121.0, height=42.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: deduct_balance(200),
    relief="flat"
)
button_5.place(x=24.0, y=209.0, width=121.0, height=42.0)

entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000000",
    highlightthickness=0,
    justify="center",
    font=("Inter Black", 12)
)
entry.place(x=642.0, y=290.0, width=129.0, height=42.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=withdraw_amount,
    relief="flat"
)
button_6.place(x=640.0, y=349.0, width=130.0, height=29.0)

window.resizable(False, False)
window.mainloop()
