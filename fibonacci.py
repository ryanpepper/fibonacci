def fib(n):
    if n < 0:
        raise ValueError('n must be greater than zero')
    elif n == 0:
        return 0
    elif round(n) != n:
        raise ValueError('n must be a positive integer and non-zero')

    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
