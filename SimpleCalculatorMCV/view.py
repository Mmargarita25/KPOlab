import customtkinter as ctk
from button import *

class CalculatorView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Калькулятор")
        self.geometry("350x550")
        self.resizable(False, False)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
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
        
        for row in button_layout:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=2)
            for char in row:
                if char.isdigit() or char == '.':
                    button = DigitButton(self.controller, char)
                elif char in '/*-+':
                    button = OperationButton(self.controller, char)
                elif char == '=':
                    button = EqualsButton(self.controller, char)
                
                btn = button.create_button(frame)
                btn.pack(side="left", padx=5)
        
        ClearButton(self.controller, "Очистить").create_button(self).pack(pady=10)
        RandomNumberButton(self.controller, "Случайное число").create_button(self).pack(pady=5)
        ClearHistoryButton(self.controller, "Удалить историю").create_button(self).pack(pady=5)
    
    def update_display(self, text):
        """Обновление отображения ввода"""
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, text)
    
    def update_history(self, history_text):
        """Обновление отображения истории"""
        self.history_label.configure(text=history_text)