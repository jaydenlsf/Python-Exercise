my_list = [5, 10, 15, 20, -25, -30]

#1
first_and_last = [my_list[0], my_list[-1]]
print(first_and_last)

#2
repeated_list = my_list * 2
print(repeated_list)

#3
my_list.reverse()
print(my_list)

#4
desc_ordered_list = sorted(my_list, reverse=True)
print(desc_ordered_list)