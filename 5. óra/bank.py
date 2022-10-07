""" Definiáljon   egy  BankSzamla()  osztályt,   ami   lehetővé   teszi   a  szamla1,  szamla2,   stb.   objektumok
létrehozását.   Az   osztály   constructora   két   példányattribútumot   inicializáljon :   a   nev   és   egyenleg
attribútumokat a 'Dupont' és 1000 alapértelmezett értékekkel.
Definiáljon három másik metódust is :
­ betesz(osszeg) adott összeget tesz a számlára
­ kivesz(osszeg) adott összeget vesz le a számláról
­ kiir() kiírja a számlatulajdonos nevét és a számlája egyenlegét.
"""

class BankSzamla:
    def __init__(self,nev,egyenleg) -> None:
        self.dupont = 1000
        self.nev = nev
        self.egyenleg = egyenleg

    def betesz(self, osszeg):
        self.egyenleg += osszeg

    def kivesz(self, osszeg):
        if osszeg > self.egyenleg:
            print("Nincs megfelelo keret")
        else:
            self.egyenleg -= osszeg

    def kiir(self):
        print("tulaj: {0}, osszeg: {1}".format(self.nev, self.egyenleg)) 

def main():
    b1 = BankSzamla("Bela", 600)

    b1.kivesz(1000)
    b1.betesz(20000)
    b1.kivesz(1000)
    b1.kiir()

if __name__ == '__main__':
    main()