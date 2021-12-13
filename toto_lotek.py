from random import randint


def lotto():
    num = []
    a = 0
    while a < 6:
        draw = randint(1, 49)
        num.append(draw)
        a = a + 1
        num.sort()
    return num


print(lotto())

