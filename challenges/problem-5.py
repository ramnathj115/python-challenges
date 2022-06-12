class InvalidCardNumberException(Exception):
    def __init__(self, card_num, message="Invalid Card Number"):
        self.card_num = card_num
        self.message = message
        super().__init__(self, self.message)

    def __str__(self):
        print(f'{self.message} : {self.card_num}')


class CardChecker:
    @staticmethod
    def is_valid_card_number(card_number: str) -> bool:
        return len(card_number) == 16 and card_number.isdigit()


class CreditCard:
    __card_num: str = None

    def __init__(self, card_num):
        self.__card_num = card_num

    def get_hidden_card_num(self) -> str:
        if CardChecker.is_valid_card_number(self.__card_num):
            return ('*' * 12) + self.__card_num[-4:]
        else:
            raise InvalidCardNumberException(self.__card_num)


if __name__ == '__main__':
    card_num_str = input("Enter the card number : ")
    obj = CreditCard(card_num_str)
    try:
        encrypted_card_number = obj.get_hidden_card_num()
    except InvalidCardNumberException as ice:
        print(ice.__str__())
    else:
        print("Encrypted Card Number : {}".format(encrypted_card_number))
