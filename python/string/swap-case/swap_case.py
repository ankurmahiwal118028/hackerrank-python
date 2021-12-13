def swap_case(s):
    y = ''
    for i in s:
        if i.isupper():
            y = y + i.lower()
        else:
            y = y + i.upper()

    return y


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)