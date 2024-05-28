
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")

# Example usage
calculator = Calculator()

result = calculator.add(5, 3)
print(result)  # Output: 8

result = calculator.subtract(10, 4)
print(result)  # Output: 6

result = calculator.multiply(2, 6)
print(result)  # Output: 12

result = calculator.divide(10, 2)
print(result)  # Output: 5