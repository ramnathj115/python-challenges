from math import pi


class ConvertRadiansToDegrees:
    __rad: float = None

    def __init__(self, rad):
        self.__rad = rad

    def convert(self):
        return self.__rad * 180 / pi


if __name__ == '__main__':
    rad = float(input("Enter the radian value : "))
    obj = ConvertRadiansToDegrees(rad)
    print("{} radians = {} degrees.".format(rad, obj.convert()))
