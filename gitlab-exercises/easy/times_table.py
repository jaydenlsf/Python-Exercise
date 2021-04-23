import pprint

n = int(input('Enter a number: '))
table = list(list(range(1*i, (n+1)*i, i)) for i in range(1, n+1))
pprint.pprint(table)