"""A collection of Fibonacci-related functions."""


def fib(n):
    """returns the (n)th Fibonacci number"""
    f = fib_generator()
    fn = 0
    for i in range(1, n + 2):
        fn = next(f)
    return fn

def fib_generator():
    a, b = 0, 1
    while True:
        yield a #the first time someone calls this generator it's going to yield a 0
        a, b = b, a + b


