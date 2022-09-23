def main():
    kartya = (1, "Priscilla", 4.5)
    id, nev, jegy = kartya
    print(kartya)
    print(id,nev,jegy)

    osztalyzat ={
        "anna" : 4.5,
        'bela' : 2,
        'cecilia': 1
    }

    print(osztalyzat.keys())
    print(osztalyzat.values())
    print(osztalyzat.items())
    print(len(osztalyzat))




if __name__ == '__main__':
    main()