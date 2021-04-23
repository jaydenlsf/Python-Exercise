print('Enter your marks for Maths, Chemistry, and Physics')
maths = int(input('Maths: '))
chem = int(input('Chemistry: '))
physics = int(input('Physics: '))
print('\n')

avg = (maths + chem + physics) / 3

grade_dict = {'D': range(40, 50), 'C': range(50, 60), 'B': range(60, 70), 'A': range(70, 100)}



for grade, mark in grade_dict.items():
    if avg < 40:
        print('\nAverage:', round(avg, 2), '%\n')
        print('You failed!')
        break
    elif avg > 100:
        print('Invalid entry(s)!')
        break
    elif avg in mark:
        print('\nAverage:', round(avg, 2), '%\n')
        print(f'Your grade: {grade}')