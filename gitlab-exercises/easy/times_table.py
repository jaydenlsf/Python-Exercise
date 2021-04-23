n = int(input('Enter a number: '))
for row in range(1, n+1):
    line = ''
    for col in range(1, n+1):
        line += '{:4}'.format(row * col)
    print(line)
