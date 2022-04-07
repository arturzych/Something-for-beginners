from random import randint


def lotto():
    num = []
    a = len(num)
    while a < 6:
        draw = randint(1, 49)
        if num.count(draw) == 0:
            num.append(draw)
        else:
            print(f'więcej niż 1 numer {draw}')
            a = a - 1
        a = a + 1
        num.sort()
    print(num)
    return num


print(lotto())

