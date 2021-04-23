num_list = [9, 7, 8, 0, 3, 0, 6, 4, 0, 6, 1, 5]
odd_digits = []
even_digits = []

for num in enumerate(num_list):
    if num[0] % 2 == 0:
        even_digits.append(num[1])
    else:
        odd_digits.append(num[1])

checknum = 10 - ((sum(even_digits) * 3 + sum(odd_digits)) % 10)
isbn = num_list + [checknum]
string_isbn = [str(num) for num in isbn]
string_isbn = ''.join(string_isbn)

print(string_isbn[0:3], '-',string_isbn[3], '-', string_isbn[4:7], '-', string_isbn[7:12], '-', string_isbn[-1])