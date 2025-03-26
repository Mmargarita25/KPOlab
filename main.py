import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""

        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Arial", 20), justify="right")
        self.entry.pack(pady=10)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=5)
            for char in row:
                btn = ctk.CTkButton(frame, text=char, width=60, height=60, font=("Arial", 18),
                                    command=lambda ch=char: self.button_click(ch))
                btn.pack(side="left", padx=5)

        clear_btn = ctk.CTkButton(self, text="Очистить", width=280, height=40, command=self.clear)
        clear_btn.pack(pady=10)

    def button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, result)
                self.expression = str(result)
            except Exception:
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, "Ошибка")
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, ctk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
