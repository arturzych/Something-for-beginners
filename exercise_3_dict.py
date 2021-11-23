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

    print(counts)

    a = 0
    for item in counts.items():
        a += 1
        if a <= 20:
            with open('part_of_hamlet.txt', 'a') as file_2:
                file_2.write(f'{item}\n')
                print(item, a)

