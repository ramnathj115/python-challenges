class Discount:
    __mp: float = None
    __discount: int = None

    def __init__(self, mp, discount):
        self.__mp = mp
        self.__discount = discount

    def get_cost_price(self) -> float:
        return self.__mp * (100 - self.__discount) / 100


if __name__ == '__main__':
    mp = int(input("Enter MRP : "))
    discount = int(input("Enter discount % : "))
    obj = Discount(mp, discount)
    print("Cost Price : Rs. {}".format(obj.get_cost_price()))
