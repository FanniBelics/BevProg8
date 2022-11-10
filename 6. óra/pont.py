from cmath import *

"""Írjunk egy pont osztályt
    Alapértelmezetten legyenek az origón
    Írjunk függvényt ami megadja 2 pont távolságát
    Írjunk függvényt ami kiírja a pontok koordinátáját  __str__
    Írjunk olyan függvényt ami egy listányi pontból kiválogatja azokat amelyek az első negyedében vannak
    Vegyünk fel 3 pontot és döntsük el hogy alkothat-e háromszöget - erre írjunk egy függvényt
    """

class Point():

    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def dist(self,x,y):
        return sqrt((self.x - x)**2 + (self.y - y)**2)

    def dist(self, b):
        return sqrt((self.x - b.x)**2 + (self.y - b.y)**2)

    def __str__(self) -> str:
        return '({0};{1})'.format(self.x, self.y)

    def __repr__(self) -> str:
        return '({0};{1})'.format(self.x, self.y)

def first (li: list):
    li = [p for p in li if (p.x > 0 and p.y > 0)]
    return li

def main():
    a = Point(4,3)
    b = Point(-4,-3)
    c = Point(-4,3)
    print("Az on pontja {0}".format(a))
    li = first([a,b,c])
    print(li)

if __name__ == '__main__':
    main()