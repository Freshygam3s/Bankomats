import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import json


try:
    with open('kartes_dati.json', 'r') as file:
        data = json.load(file)
    print("Data loaded successfully:", data)
except FileNotFoundError:
    messagebox.showerror("Error", "JSON file not found!")
    data = {"cards": []}

LANGUAGES = {
    "ENG": {
        "pin": "PIN:",
        "withdraw": "Withdraw",
        "deposit": "Deposit",
        "check_balance": "Check Balance",
        "exit": "Exit",
        "success": "Success",
        "error": "Error",
        "invalid_pin": "Invalid PIN!",
        "insufficient_balance": "Insufficient balance!",
        "withdrawn": "Withdrawn ${amount}. New balance: ${balance}",
        "deposited": "Deposited ${amount}. New balance: ${balance}",
        "balance": "Your current balance is: ${balance}",
        "enter_amount_withdraw": "Enter amount to withdraw:",
        "enter_amount_deposit": "Enter amount to deposit:",
        "account_info": "Account Information",
        "name": "Name:",
        "card_number": "Card Number:",
        "view_account_info": "View Account Info",
        "Wrong": "Too many incorrect attempts. Exiting.",
    },
    "LV": {
        "pin": "PIN:",
        "withdraw": "Izņemt naudu",
        "deposit": "Iemaksāt naudu",
        "check_balance": "Pārbaudīt atlikumu",
        "exit": "Iziet",
        "success": "Veiksmīgi",
        "error": "Kļūda",
        "invalid_pin": "Nepareizs PIN!",
        "insufficient_balance": "Nepietiekams atlikums!",
        "withdrawn": "Izņemti ${amount}. Jauns atlikums: ${balance}",
        "deposited": "Iemaksāti ${amount}. Jauns atlikums: ${balance}",
        "balance": "Jūsu pašreizējais atlikums ir: ${balance}",
        "enter_amount_withdraw": "Ievadiet izņemamo summu:",
        "enter_amount_deposit": "Ievadiet iemaksājamo summu:",
        "account_info": "Konta informācija",
        "name": "Vārds:",
        "card_number": "Kartes numurs:",
        "view_account_info": "Skatīt konta informāciju",
        "Wrong": "Pārāk daudz nepareizi Pin. Aizverās.",
    },
    "RUS": {
        "pin": "ПИН:",
        "withdraw": "Снять деньги",
        "deposit": "Внести деньги",
        "check_balance": "Проверить баланс",
        "exit": "Выйти",
        "success": "Успех",
        "error": "Ошибка",
        "invalid_pin": "Неверный ПИН!",
        "insufficient_balance": "Недостаточно средств!",
        "withdrawn": "Снято ${amount}. Новый баланс: ${balance}",
        "deposited": "Внесено ${amount}. Новый баланс: ${balance}",
        "balance": "Ваш текущий баланс: ${balance}",
        "enter_amount_withdraw": "Введите сумму для снятия:",
        "enter_amount_deposit": "Введите сумму для внесения:",
        "account_info": "Информация о счете",
        "name": "Имя:",
        "card_number": "Номер карты:",
        "view_account_info": "Просмотреть информацию о счете",
        "Wrong": "Слишком много неверных попыток. Выход из системы.",
    }
}

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank ATM")
        self.root.geometry("1500x800")
        self.root.configure(bg="purple")

        self.PIN_var = tk.StringVar()
        self.current_card = None
        self.transaction_window = None
        self.current_language = "ENG"

        self.create_frames()
        self.create_widgets()
        self.create_buttons()

        self.attempts = 0

    def create_frames(self):
        self.PIN_frame = tk.Frame(self.root, bg="purple")
        self.lang_frame = tk.Frame(self.root, bg="purple")
        self.button_frame = tk.Frame(self.root, bg="purple")
        self.button_frame_1 = tk.Frame(self.root, bg="purple")
        self.button_frame_2 = tk.Frame(self.root, bg="purple")
        self.button_frame_3 = tk.Frame(self.root, bg="purple")

    def create_widgets(self):
        self.PIN_label = tk.Label(self.PIN_frame, text=LANGUAGES[self.current_language]["pin"], bg="purple", font=("Arial", 35, "bold"))
        self.PIN_entry = tk.Entry(self.PIN_frame, show="*", font=("Arial", 15), textvariable=self.PIN_var)

        # Pack widgets
        self.PIN_label.pack(side="left", padx=10)
        self.PIN_entry.pack(side="left", padx=10)
        self.PIN_frame.pack(pady=20)

    def create_buttons(self):
        self.load_language_buttons()
        self.lang_frame.pack(pady=10)

        self.create_number_buttons()
        self.button_frame.pack(pady=10)
        self.button_frame_1.pack(pady=10)
        self.button_frame_2.pack(pady=10)
        self.button_frame_3.pack(pady=10)

    def load_language_buttons(self):
        try:
            self.eng_img = self.load_image("images/eng.png", (50, 30))
            self.lv_img = self.load_image("images/lv.png", (50, 30))
            self.rus_img = self.load_image("images/rus.jpeg", (50, 30))

            self.eng_btn = tk.Button(self.lang_frame, image=self.eng_img, text="ENG", compound="center", bg="black", font="bold", command=lambda: self.switch_language("ENG"))
            self.eng_btn.pack(side="left", padx=5)
            self.lv_btn = tk.Button(self.lang_frame, image=self.lv_img, text="LV", compound="center", bg="black", font="bold", command=lambda: self.switch_language("LV"))
            self.lv_btn.pack(side="left", padx=5)
            self.rus_btn = tk.Button(self.lang_frame, image=self.rus_img, text="RUS", compound="center", bg="black", font="bold", command=lambda: self.switch_language("RUS"))
            self.rus_btn.pack(side="left", padx=5)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load images: {e}")

    def load_image(self, path, size):
        image = Image.open(path)
        image = image.resize(size)
        return ImageTk.PhotoImage(image)

    def create_number_buttons(self):
        buttons = [
            ("1", "2", "3", self.button_frame),
            ("4", "5", "6", self.button_frame_1),
            ("7", "8", "9", self.button_frame_2),
            ("DEL", "0", "Enter", self.button_frame_3)
        ]

        for row in buttons:
            for text in row[:3]:
                if text == "Enter":
                    btn = tk.Button(row[3], text=text, height=5, width=10, command=self.enter_func)
                elif text == "DEL":
                    btn = tk.Button(row[3], text=text, height=5, width=10, command=self.delete_func)
                else:
                    btn = tk.Button(row[3], text=text, height=5, width=10, command=lambda t=text: self.append_pin(t))
                btn.configure(bg="white", borderwidth=9)
                btn.pack(side="left", padx=5, pady=5)

    def append_pin(self, value):
        current_pin = self.PIN_var.get()
        self.PIN_var.set(current_pin + value)

    def delete_func(self):
        current_pin = self.PIN_var.get()
        self.PIN_var.set(current_pin[:-1])

    def enter_func(self):
        entered_pin = self.PIN_var.get()
        MAX_ATTEMPTS = 3
        if self.validate_pin(entered_pin):
            messagebox.showinfo(LANGUAGES[self.current_language]["success"], "PIN is correct!")
            self.attempts = 0
            self.open_transaction_window()
        else:
            self.attempts += 1
            messagebox.showerror(LANGUAGES[self.current_language]["error"], LANGUAGES[self.current_language]["invalid_pin"])
            if self.attempts>=MAX_ATTEMPTS:
              messagebox.showerror(LANGUAGES[self.current_language]["error"],LANGUAGES[self.current_language]["Wrong"])
              root.destroy()
                
    def validate_pin(self, entered_pin):
        for card in data.get("cards", []):
            if card.get("pin") == entered_pin:
                self.current_card = card
                return True
        return False

    def open_transaction_window(self):
        self.root.withdraw()

        self.transaction_window = tk.Toplevel(self.root)
        self.transaction_window.title("Transaction Window")
        self.transaction_window.geometry("1500x800")
        self.transaction_window.state("zoomed")
        self.transaction_window.configure(bg="purple")

        self.transaction_window.protocol("WM_DELETE_WINDOW", self.close_transaction_window)

        withdraw_btn = tk.Button(self.transaction_window, text=LANGUAGES[self.current_language]["withdraw"], font=("Arial", 20), command=self.withdraw)
        withdraw_btn.pack(pady=10)

        deposit_btn = tk.Button(self.transaction_window, text=LANGUAGES[self.current_language]["deposit"], font=("Arial", 20), command=self.deposit)
        deposit_btn.pack(pady=10)

        balance_btn = tk.Button(self.transaction_window, text=LANGUAGES[self.current_language]["check_balance"], font=("Arial", 20), command=self.check_balance)
        balance_btn.pack(pady=10)

        account_info_btn = tk.Button(self.transaction_window, text=LANGUAGES[self.current_language]["view_account_info"], font=("Arial", 20), command=self.show_account_info)
        account_info_btn.pack(pady=10)

        exit_btn = tk.Button(self.transaction_window, text=LANGUAGES[self.current_language]["exit"], font=("Arial", 20), command=self.close_transaction_window)
        exit_btn.pack(pady=10)

    def close_transaction_window(self):
        self.transaction_window.destroy()
        self.PIN_var.set("")
        self.root.deiconify()
        root.state("zoomed")

    def withdraw(self):
        amount = simpledialog.askinteger(
            LANGUAGES[self.current_language]["withdraw"],
            LANGUAGES[self.current_language]["enter_amount_withdraw"]
        )
        if amount is not None:
            if amount > self.current_card["balance"]:
                messagebox.showerror(LANGUAGES[self.current_language]["error"], LANGUAGES[self.current_language]["insufficient_balance"])
            else:
                self.current_card["balance"] -= amount
                messagebox.showinfo(LANGUAGES[self.current_language]["success"], LANGUAGES[self.current_language]["withdrawn"].format(amount=amount, balance=self.current_card['balance']))

    def deposit(self):
        amount = simpledialog.askinteger(
            LANGUAGES[self.current_language]["deposit"],
            LANGUAGES[self.current_language]["enter_amount_deposit"]
        )
        if amount is not None:
            self.current_card["balance"] += amount
            messagebox.showinfo(LANGUAGES[self.current_language]["success"], LANGUAGES[self.current_language]["deposited"].format(amount=amount, balance=self.current_card['balance']))

    def check_balance(self):
        messagebox.showinfo(LANGUAGES[self.current_language]["balance"], LANGUAGES[self.current_language]["balance"].format(balance=self.current_card['balance']))

    def show_account_info(self):
        account_info_window = tk.Toplevel(self.transaction_window)
        account_info_window.title(LANGUAGES[self.current_language]["account_info"])
        account_info_window.geometry("400x200")
        account_info_window.configure(bg="lightblue")

        name_label = tk.Label(account_info_window, text=f"{LANGUAGES[self.current_language]['name']} {self.current_card['name']}", font=("Arial", 16), bg="lightblue")
        name_label.pack(pady=10)

        card_number_label = tk.Label(account_info_window, text=f"{LANGUAGES[self.current_language]['card_number']} {self.current_card['card_number']}", font=("Arial", 16), bg="lightblue")
        card_number_label.pack(pady=10)

        ok_button = tk.Button(account_info_window, text="OK", font=("Arial", 16), command=account_info_window.destroy)
        ok_button.pack(pady=20)

    def switch_language(self, language):
        self.current_language = language
        self.update_ui_text()

    def update_ui_text(self):
        self.PIN_label.config(text=LANGUAGES[self.current_language]["pin"])
        if self.transaction_window:
            for widget in self.transaction_window.winfo_children():
                if isinstance(widget, tk.Button):
                    if widget["text"] == "Withdraw":
                        widget.config(text=LANGUAGES[self.current_language]["withdraw"])
                    elif widget["text"] == "Deposit":
                        widget.config(text=LANGUAGES[self.current_language]["deposit"])
                    elif widget["text"] == "Check Balance":
                        widget.config(text=LANGUAGES[self.current_language]["check_balance"])
                    elif widget["text"] == "View Account Info":
                        widget.config(text=LANGUAGES[self.current_language]["view_account_info"])
                    elif widget["text"] == "Exit":
                        widget.config(text=LANGUAGES[self.current_language]["exit"])

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = ATMApp(root)
    root.mainloop()
