#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818d

def main():
    li = [n*2 for n in range(0,10)]

    for n in range(0,10):
        li.append(n*2)

    print(li)

    li2 = ['auto', 'villamos', 'metro']
    li2 = [s.upper()+'!' for s in li2]
    li.clear()
    for s in li2:
        s = s.upper() + '!'
        li.append(s)
    print(li2)

if __name__ == '__main__':
    main()