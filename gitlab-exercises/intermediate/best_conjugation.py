file = open("gitlab-exercises\intermediate\words.txt")
words = file.readlines()


def subword(string):
    subwords = []
    for word in words:
        if string.find(word) == -1:
            continue
        else:
            subwords.append(word)
        print(subwords)


subword("gantare")
