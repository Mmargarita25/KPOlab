import customtkinter as ctk
from random import choice

# v1.0.0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Крутой калькулятор")
        self.geometry("300x450")
        self.resizable(False, False)

        # Список для хранения истории вычислений
        self.history = []
        self.expression = ""

        # Добавим лейбл для отображения истории
        self.history_label = ctk.CTkLabel(self, text="", height=20, font=("Arial", 12))
        self.history_label.pack(pady=(10, 0))

        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Arial", 24), justify="right")
        self.entry.pack(pady=10)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        # Цвета для операторов
        operator_color = "#808080"  # Серый
        equals_color = "#32CD32"

        for row in buttons:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=2)
            for char in row:
                if char in '/*-+':
                    color = operator_color
                elif char == '=':
                    color = equals_color
                else:
                    color = None  # Будет использоваться цвет по умолчанию

                btn = ctk.CTkButton(frame, text=char, width=60, height=60, font=("Arial", 20),
                                    fg_color=color, hover_color="#5D5D5D" if color else None,
                                    command=lambda ch=char: self.button_click(ch))
                btn.pack(side="left", padx=5)

        # Кнопка очистки красного цвета с эффектом при наведении
        clear_btn = ctk.CTkButton(self, text="Очистить", width=280, height=40,
                                  fg_color="#FF0000", hover_color="#CC0000",
                                  font=("Arial", 16, "bold"),
                                  command=self.clear)
        clear_btn.pack(pady=10)

        # Кнопка для случайного числа
        random_btn = ctk.CTkButton(self, text="Случайное число", width=280, height=30,
                                   fg_color="#4B0082", hover_color="#800080",
                                   command=self.generate_random)
        random_btn.pack(pady=5)

    def button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                # Сохраняем в историю
                self.history.append(f"{self.expression} = {result}")
                if len(self.history) > 3:
                    self.history.pop(0)
                self.update_history()

                self.entry.delete(0, ctk.END)
                self.entry.insert(0, result)
                self.expression = str(result)
            except Exception:
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, "Ошибка!!!")
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, ctk.END)

    def generate_random(self):
        random_num = choice(range(1, 1001))
        self.expression = str(random_num)
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, random_num)

    def update_history(self):
        history_text = " | ".join(self.history[-3:])
        self.history_label.configure(text=history_text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()