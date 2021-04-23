n = int(input('Enter a number: '))
table = list(list(range(1*i, (n+1)*i, i)) for i in range(1, n+1))

for i in table:
    i = [str(j).rjust(len(str(table[-1][-1])) + 1) for j in i]
    print(''.join(i))