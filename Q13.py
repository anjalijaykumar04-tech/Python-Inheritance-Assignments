class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

class AdvancedCalculator(Calculator):
    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")

c = AdvancedCalculator()

c.add(10, 5)
c.subtract(10, 5)
c.multiply(10, 5)
c.divide(10, 5)