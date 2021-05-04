def fibo(n):

    if n < 0:
        return ((-1) ** (n + 1)) * fibo(-n)

    if n == 1:
        return n
    elif n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)