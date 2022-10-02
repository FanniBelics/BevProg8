##készítsük el while segítségével az lnko függvényt, majd rekurzívan

def lnko(a,b):
    if(a > b):
        return lnko(a-b, b)
    elif (a < b):
        return lnko(a, b-a)
    else:
        return a

def main():
    a = 64
    b = 16

    a = lnko(a,b)

    print(a)

if __name__ == '__main__':
    main()