class Reporter:
    def __enter__(self):  # 2b. po wywłaniu wykonuje się na początku ta funkcja (magic method)
        print('A')
        return self

    def __exit__(self, type, value, traceback):
        print('B')  # 4. wykonuje się na końcu bloku "with"


print('F')  # 1. Wykona się jako pierwsze


with Reporter():  # 2a. wywołanie klasy
    print('D')     # 3. wykonuje się po wyjściu z metody "enter"

print('E')  # 5.
print('C')  # 6.
