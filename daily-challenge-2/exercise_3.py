my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([i[1] for i in enumerate(my_list) if i[0] % 2 == 0])