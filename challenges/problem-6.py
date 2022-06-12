class EqualNotEqual:
    __pattern: str = None

    def __init__(self, pattern):
        self.__pattern = pattern

    def is_equal(self) -> bool:
        return len(list(filter(lambda ch: ch == 'X', self.__pattern))) == len(
            list(filter(lambda ch: ch == 'O', self.__pattern)))


if __name__ == '__main__':
    pattern = input("Enter the pattern : ")
    obj = EqualNotEqual(pattern)
    print("Equal no. of Xs and Os") if obj.is_equal() else print("Unequal no. of Xs and Os")
