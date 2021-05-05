def upper_letters(string):
    upper = []
    for index, char in enumerate(string):
        if char.isupper():
            upper.append((char, index))
    return upper


print(upper_letters("HeLlO wOrLd!"))
