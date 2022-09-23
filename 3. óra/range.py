def main():
    for x in range(0, 5, 2):
        print(x)

    li = ["alma", 'körte', 'szilva', 'szőlő']
    for x in li:
        print(x)
    i = 1
    while i < 15:
        if((i % 2 == 0) and (i % 3 == 0)):
            break
        print(i)
        i += 1
    

if __name__ == '__main__':
    main()