import customtkinter as ctk
from button import *

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("350x550")
        self.resizable(False, False)
        
        # Установка темного режима
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.history = []
        self.expression = ""
        
        # Создаем UI элементы
        self.create_widgets()
        self.create_buttons()
    
    def create_widgets(self):
        """Создание основных виджетов интерфейса"""
        self.history_label = ctk.CTkLabel(self, text="", height=20, font=("Arial", 12))
        self.history_label.pack(pady=(10, 0))
        
        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Arial", 24), justify="right")
        self.entry.pack(pady=10)
        self.entry.insert(0, "0")
    
    def create_buttons(self):
        """Создание кнопок с помощью фабрики"""
        button_layout = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        # Создаем кнопки цифр и операций
        for row in button_layout:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=2)
            for char in row:
                if char.isdigit() or char == '.':
                    button = DigitButton(self, char)
                elif char in '/*-+':
                    button = OperationButton(self, char)
                elif char == '=':
                    button = EqualsButton(self, char)
                
                btn = button.create_button(frame)
                btn.pack(side="left", padx=5)
        
        # Создаем специальные кнопки
        ClearButton(self, "Очистить").create_button(self).pack(pady=10)
        RandomNumberButton(self, "Случайное число").create_button(self).pack(pady=5)
        ClearHistoryButton(self, "Удалить историю").create_button(self).pack(pady=5)
    
    def update_display(self):
        """Обновление отображения ввода"""
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, self.expression if self.expression else "0")
    
    def update_history(self):
        """Обновление отображения истории"""
        history_text = " | ".join(self.history[-3:])
        self.history_label.configure(text=history_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()