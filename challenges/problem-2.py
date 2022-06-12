class ListSort:
    __lst: list = None

    def __init__(self, lst):
        self.__lst = lst

    def sort_list_asc(self):
        self.__lst = sorted(self.__lst)

    def sort_list_desc(self):
        self.__lst = sorted(self.__lst, reverse=True)

    def print_list(self):
        print(", ".join(map(str, self.__lst)))


if __name__ == '__main__':
    lst = list(map(int, input("Enter a list of integers : ").split()))
    obj = ListSort(lst)
    attempt_count = 4
    while True:
        choice_str = input("Enter sorting choice(asc/desc/none) : ")
        try:
            if choice_str == 'asc':
                obj.sort_list_asc()
            elif choice_str == 'desc':
                obj.sort_list_desc()
            elif choice_str == 'none':
                pass
            else:
                raise ValueError("Invalid Choice")
        except ValueError as e:
            attempt_count -= 1
            if attempt_count > 0:
                print(f'{e.__str__()}...Try again {attempt_count} remaining attempts.')
                continue
            else:
                print("Exhausted number of attempts !!!")
                break
        else:
            obj.print_list()
            break
