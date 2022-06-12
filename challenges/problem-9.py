class NumberFilter:
    __lst: list = None

    def __init__(self, lst):
        self.__lst = lst

    def get_filtered_list(self) -> list:
        return list(filter(lambda x: x.isdigit(), self.__lst))


if __name__ == '__main__':
    lst = input("Enter a list of integers and strings : ").split()
    obj = NumberFilter(lst)
    print("Filtered List : {}".format(obj.get_filtered_list()))
