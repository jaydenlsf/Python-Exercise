my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Please enter a number: "))

less_than_5 = [i for i in my_list if i < 5]
print(less_than_5)

less_than_user = [i for i in my_list if i < num]
print(less_than_user)