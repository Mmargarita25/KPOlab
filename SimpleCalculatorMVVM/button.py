import customtkinter as ctk
from abc import ABC, abstractmethod
from commands import *

class Button(ABC):
    """Абстрактный класс кнопки"""
    def __init__(self, calculator, char):
        self.calculator = calculator
        self.char = char
        self.command = self.create_command()
    
    @abstractmethod
    def create_command(self):
        """Фабричный метод для создания команды"""
        pass
    
    def create_button(self, frame):
        """Создание визуальной кнопки"""
        return ctk.CTkButton(
            frame, 
            text=self.char, 
            width=self.get_width(), 
            height=self.get_height(), 
            font=self.get_font(),
            fg_color=self.get_color(),
            hover_color=self.get_hover_color(),
            command=self.command.execute
        )
    
    def get_width(self):
        return 60
    
    def get_height(self):
        return 60
    
    def get_font(self):
        return ("Arial", 20)
    
    def get_color(self):
        return None
    
    def get_hover_color(self):
        return None

class DigitButton(Button):
    """Кнопка цифры"""
    def create_command(self):
        return AppendDigitCommand(self.calculator, self.char)

class OperationButton(Button):
    """Кнопка операции"""
    def create_command(self):
        return AppendOperationCommand(self.calculator, self.char)
    
    def get_color(self):
        return "#808080"
    
    def get_hover_color(self):
        return "#5D5D5D"

class EqualsButton(Button):
    """Кнопка равно"""
    def create_command(self):
        return EvaluateCommand(self.calculator)
    
    def get_color(self):
        return "#32CD32"
    
    def get_hover_color(self):
        return "#228B22"

class ClearButton(Button):
    """Кнопка очистки"""
    def create_command(self):
        return ClearCommand(self.calculator)
    
    def get_width(self):
        return 280
    
    def get_height(self):
        return 40
    
    def get_font(self):
        return ("Arial", 16, "bold")
    
    def get_color(self):
        return "#FF0000"
    
    def get_hover_color(self):
        return "#CC0000"

class ClearHistoryButton(Button):
    """Кнопка очистки истории"""
    def create_command(self):
        return ClearHistoryCommand(self.calculator)
    
    def get_width(self):
        return 280
    
    def get_height(self):
        return 30
    
    def get_color(self):
        return "#FF4500"
    
    def get_hover_color(self):
        return "#FF6347"

class RandomNumberButton(Button):
    """Кнопка случайного числа"""
    def create_command(self):
        return RandomNumberCommand(self.calculator)
    
    def get_width(self):
        return 280
    
    def get_height(self):
        return 30
    
    def get_color(self):
        return "#4B0082"
    
    def get_hover_color(self):
        return "#800080"