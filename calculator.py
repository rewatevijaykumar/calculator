class Calculator:
    def __init__(self):
        self.num1 = int(input("Enter the first number : "))
        self.num2 = int(input("Enter the second number : "))

    def add(self) -> str:
        res = self.num1 + self.num2
        result = f'sum of {str(self.num1)} and {str(self.num2)} is {str(res)}'
        print(result)
        return result

    def subtract(self) -> str:
        res = self.num1 - self.num2
        result = f'difference of {str(self.num1)} and {str(self.num2)} is {str(res)}'
        print(result)
        return result

    def multiply(self) -> str:
        res = self.num1 * self.num2
        result = f'product of {str(self.num1)} and {str(self.num2)} is {str(res)}'
        print(result)
        return result

    def divide(self) -> str:
        res = self.num1 / self.num2
        result = f'division of {str(self.num1)} and {str(self.num2)} is {str(res)}'
        print(result)
        return result


if __name__ == '__main__':
    operation = Calculator()
    operation.add()
    operation.subtract()
    operation.multiply()
    operation.divide()