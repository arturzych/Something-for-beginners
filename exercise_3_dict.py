import string

with open('hamlet2.txt') as file:
    counts = dict()
    for line in file:
        words = line.split()
        print(words)
        for word in words:
            punc = str.maketrans('', '', string.punctuation)
            word = word.translate(punc)
            word = word.lower()
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    # print(counts)
    # c = dict(counts)
    # print(c)

    a = 0

    for item in counts.items():
        a += 1
        if a <= 20:
            print(item, a)
