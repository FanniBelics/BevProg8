def both_ends(stri):
    if(len(stri) < 2):
        return ''

    return (stri[0:2] + stri[-2:])

def main():
    # txt = "Hello, world!"
    # print(len(txt))
    # print(txt[3])
    # print(txt[1:8])
    # print(txt.upper())
    # print(txt.capitalize())
    # print(txt.title())
    # print("          hehe          ".strip())
    # print(txt.replace("l", "n"))
    # print("1;2;3;4;5".split(sep=';'))
    # print(txt.rfind('o'))
    # print(txt.join("henlo"))
    # txt = 'he\'s boy'

    print(both_ends('edcgvhzbjlba'))


if __name__ == '__main__':
    main()