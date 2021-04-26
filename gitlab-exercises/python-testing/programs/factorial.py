def fact(x):
    if x == 0:
        return 1
    elif x < 0:
        return "Invalid input"
    return x * fact(x - 1)


print(fact(5))
print(fact(-2))
