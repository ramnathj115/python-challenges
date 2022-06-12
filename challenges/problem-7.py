class InvalidOperatorException(Exception):
    def __init__(self, op, message='Invalid Operator'):
        self.op = op
        self.message = message
        super().__init__(self, self.message)

    def __str__(self):
        print(f'{self.message} {self.op}')


class Calculator:
    __a: int = None
    __b: int = None

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self) -> int:
        return self.__a + self.__b

    def subtract(self) -> int:
        return self.__a - self.__b

    def multiply(self) -> int:
        return self.__a * self.__b

    def divide(self) -> float:
        return self.__a / self.__b


if __name__ == '__main__':
    print("Calculator")
    print("==========")
    a, op, b = input("Enter : ").split()
    obj = Calculator(int(a), int(b))
    res = None
    try:
        if op == '+':
            res = obj.add()
        elif op == '-':
            res = obj.subtract()
        elif op == '*':
            res = obj.multiply()
        elif op == '/':
            res = obj.divide()
        else:
            raise InvalidOperatorException(op)
    except InvalidOperatorException as ioe:
        print(ioe.__str__())
    else:
        print("Result : {}".format(res))
