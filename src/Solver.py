import math


class Solver:
    def __init__(self):
        pass

    def calculate(self, a, b, c):
        # type: (object, object, object) -> object
            d = b ** 2 - 4 * a * c
            if d >= 0:
                disc = math.sqrt(d)
                root1 = (-b + disc) / (2 * a)
                root2 = (-b - disc) / (2 * a)
                print (root1, root2)
            else:
                print ("invalid quadratic equation")


while True:
    a = int(input("a "))
    b = int(input("b "))
    c = int(input("c "))

    Solver().calculate(a, b, c)
