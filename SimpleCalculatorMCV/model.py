class CalculatorModel:
    def __init__(self):
        self.history = []
        self.expression = "0"
    
    def append_to_expression(self, value):
        if self.expression == "0":
            self.expression = value
        else:
            self.expression += value
    
    def set_expression(self, value):
        self.expression = value
    
    def clear_expression(self):
        self.expression = "0"
    
    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.add_to_history(f"{self.expression} = {result}")
            self.expression = str(result)
            return True, result
        except Exception:
            self.expression = ""
            return False, "Ошибка"
    
    def add_to_history(self, entry):
        self.history.append(entry)
        if len(self.history) > 3:
            self.history.pop(0)
    
    def clear_history(self):
        self.history = []
    
    def get_history_text(self):
        return " | ".join(self.history)
    
    def get_expression(self):
        return self.expression if self.expression else "0"