word = 'hemoglobina to cząsteczka białka w krwinkach czrwonych, ' \
       'ktora przenosi tlen z płuc do tkanek organizmu i zwraca dwutlenek węgla' \
       'z powrotem do płuc'
d = dict()

for item in word:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1
print(f' Jestem tutaj {d}')

# Drugi sposób poprzez użycie metody get() - Jeśli klucz pojawia się w słowniku get() zwraca odpowiednią wartość
# w przeciwnym razie wartość pozostaje domyślna # w ten sposób unikamy rozbudowanego kodu
# w postaci wprowadzania warunku if

# for item in word:
#     d[item] = d.get(item, 0) + 1
# print(d)


def info(x, y=1, z=2):

    return f'{x}, {y}, {z}'


print(info(4, z=3, y=6))



for i in range(100):

    if 20 <= i <= 40 and i % 5 == 0:
        print(i)

