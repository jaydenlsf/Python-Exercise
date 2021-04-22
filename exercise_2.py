num = float(input('Enter a number: '))
check = float(input('Enter another number: '))

if num % 4 == 0:
    print(f'{num} is divisible by 4.')
elif num % 2 == 0:
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')

if num % check == 0:
    print(f'{num} is divisible by {check}')
else:
    print(f'{num} is not divisible by {check}')