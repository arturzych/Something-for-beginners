a = 0
while a < 15:
    a = a + 1
    print(a)

b = [1, 2]
c = [3, 4]
print([1, 2].extend([3, 4]))
[1, 2].extend(c)
print(b)
print([1, 2])


