import argparse


class Calculator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

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
    # initializing parser
    parser = argparse.ArgumentParser(description='calculator arguments')

    # Adding Argument
    parser.add_argument('-num1', '--number1', required=True, type=float, help="Enter an integer for first number")
    parser.add_argument('-num2', '--number2', required=True, type=float, help="Enter an integer for second number")

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)

    operation = Calculator(args.number1, args.number2)
    operation.add()
    operation.subtract()
    operation.multiply()
    operation.divide()
