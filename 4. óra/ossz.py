def ossz(li):
    if len(li) == 1:
        return li[0]
    return li[0] + ossz(li[1:])

def main():
    print(ossz([1,2,3,4,5]))

if __name__ == '__main__':
    main()