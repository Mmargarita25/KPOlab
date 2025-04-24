from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)
    
    def run(self):
        self.view.mainloop()
    
    def append_to_expression(self, value):
        self.model.append_to_expression(value)
        self.view.update_display(self.model.get_expression())
    
    def set_expression(self, value):
        self.model.set_expression(value)
        self.view.update_display(self.model.get_expression())
    
    def clear_expression(self):
        self.model.clear_expression()
        self.view.update_display(self.model.get_expression())
    
    def evaluate_expression(self):
        success, result = self.model.evaluate_expression()
        self.view.update_display(result)
        self.view.update_history(self.model.get_history_text())
    
    def clear_history(self):
        self.model.clear_history()
        self.view.update_history(self.model.get_history_text())
    
    def add_to_history(self, entry):
        self.model.add_to_history(entry)
        self.view.update_history(self.model.get_history_text())