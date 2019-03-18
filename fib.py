def fib(n):
    f = [0, 1]
    for i in range(n):
        f.append(f[-1] + f[-2])
    return f
