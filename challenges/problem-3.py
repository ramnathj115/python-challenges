class DecimalToBinary:
    __num: int = None

    def __init__(self, num):
        self.__num = num

    def convert(self) -> int:
        bin_str = ''
        if not self.__num:
            return 0
        while self.__num > 0:
            bin_str = bin_str + str(self.__num % 2)
            self.__num //= 2
        return int(bin_str[::-1])


if __name__ == '__main__':
    n = int(input("Enter the decimal : "))
    obj = DecimalToBinary(n)
    print("Binary Representation : {}".format(obj.convert()))
