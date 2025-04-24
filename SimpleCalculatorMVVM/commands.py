from abc import ABC, abstractmethod
import random

class Command(ABC):
    """Абстрактный класс команды"""
    @abstractmethod
    def execute(self):
        pass

class AppendDigitCommand(Command):
    """Команда добавления цифры"""
    def __init__(self, calculator, digit):
        self.calculator = calculator
        self.digit = digit
    
    def execute(self):
        if self.calculator.expression == "0":
            self.calculator.expression = self.digit
        else:
            self.calculator.expression += self.digit
        self.calculator.update_display()

class AppendOperationCommand(Command):
    """Команда добавления операции"""
    def __init__(self, calculator, operation):
        self.calculator = calculator
        self.operation = operation
    
    def execute(self):
        if self.calculator.expression and self.calculator.expression[-1] not in '/*-+':
            self.calculator.expression += self.operation
            self.calculator.update_display()

class EvaluateCommand(Command):
    """Команда вычисления выражения"""
    def __init__(self, calculator):
        self.calculator = calculator
    
    def execute(self):
        try:
            result = eval(self.calculator.expression)
            self.calculator.history.append(f"{self.calculator.expression} = {result}")
            if len(self.calculator.history) > 3:
                self.calculator.history.pop(0)
            self.calculator.update_history()
            
            self.calculator.expression = str(result)
            self.calculator.update_display()
        except Exception:
            self.calculator.expression = ""
            self.calculator.entry.delete(0, 'end')
            self.calculator.entry.insert(0, "Ошибка")

class ClearCommand(Command):
    """Команда очистки"""
    def __init__(self, calculator):
        self.calculator = calculator
    
    def execute(self):
        self.calculator.expression = ""
        self.calculator.update_display()

class ClearHistoryCommand(Command):
    """Команда очистки истории"""
    def __init__(self, calculator):
        self.calculator = calculator
    
    def execute(self):
        self.calculator.history = []
        self.calculator.update_history()

class RandomNumberCommand(Command):
    """Команда генерации случайного числа"""
    def __init__(self, calculator):
        self.calculator = calculator
    
    def execute(self):
        random_num = random.choice(range(1, 1001))
        self.calculator.expression = str(random_num)
        self.calculator.update_display()