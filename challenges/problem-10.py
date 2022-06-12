class RepeatChar:
    __st: str = None

    def __init__(self, st):
        self.__st = st

    def get_repeated_string(self) -> str:
        return "".join([ch * 2 for ch in self.__st])


if __name__ == '__main__':
    st = input("Enter the string : ")
    obj = RepeatChar(st)
    print("Repeated String : {}".format(obj.get_repeated_string()))
