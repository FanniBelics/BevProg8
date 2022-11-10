from enum import Enum


class Field(Enum):
    HOUSE = 'house',
    GARDEN = 'garden',
    TREE = 'tree'

class Place:

    def __init__(self,begin, end, type) -> None:
        self.begin = min(begin,end)
        self.end = max(begin,end)
        self.type = type

    def distance(self) -> float:
        return self.end - self.begin

    def __str__(self) -> str:
        return "({0};{1})".format(self.begin, self.end)

    def __add__(self, b) -> 'Place': # self + b
        newElement = Place(min(self.begin, b.begin), max(self.end,b.end))
        return newElement
    
    def __sub__(self, b): # self - b
        newElement = Place(max(self.begin, b.begin), min(self.end,b.end))
        return newElement

    def __ge__(self,b): # Greater Equal >=
        if self.distance() >= b.distance():
            return True
        else:
            return False

    #def __iadd__(self, b): #self += b
    # __eq__(self,b): self == b    

def main():
    pass

if __name__ == "__main__":
    main()
