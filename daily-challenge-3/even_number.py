def even_num(start, end):
    even_num_list = []
    even_digits = []

    if start > end:
        start, end = end, start

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_num_list.append(str(num))

    for s in even_num_list:
        if len(s) == 1:
            even_digits.append(s)
        elif len(s) > 3:
            continue
        elif int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0:
            even_digits.append(s)

    return ", ".join(even_digits)
