class VowelCheck:
    @staticmethod
    def is_vowel(ch) -> bool:
        return ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "U"]


class Vowels:
    __st: str = None

    def __init__(self, st):
        self.__st = st

    def get_vowels(self) -> (list, int):
        vowels_list = list(filter(VowelCheck.is_vowel, self.__st))
        return vowels_list, len(vowels_list)


if __name__ == '__main__':
    st = input("Enter the string: ")
    obj = Vowels(st)
    result: (list, int) = obj.get_vowels()
    print("Vowels in {} : {}".format(st, result[0]))
    print("Number of Vowels : ", result[1])
