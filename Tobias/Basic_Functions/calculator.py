import math

class Calculator():
    def __init__(self):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return float(self.number1) + float(self.number2)

    def subtract(self):
        return float(self.number1) - float(self.number2)

    def multiply(self):
        return float(self.number1) * float(self.number2)

    def divide(self):
        return float(self.number1) / float(self.number2)

    def computePowers(self):
        return float(self.number1) ** float(self.number2)

    def get_pi(self):
        return float(math.pi)

    def get_e(self):
        return float(math.e)

    def computeLogs(self):
        return float(math.log(float(self.number2), float(self.number1)))

    def computeFactorials(self):
        return float(math.factorial(float(self.number1)))

    def sin(self):
        return float(math.sin(float(self.number1)))

    def cos(self):
        return float(math.cos(float(self.number1)))

    def tan(self):
        return float(math.tan(float(self.number1)))

