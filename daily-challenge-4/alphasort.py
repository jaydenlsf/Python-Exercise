def alphasort(string):
    word_list = string.split(" ")
    unique_words = set(word_list)
    unique_word_list = list(unique_words)
    sorted_list = sorted(unique_word_list)

    return " ".join(sorted_list)


print(alphasort("hello world practice makes perfect and hello world again"))
