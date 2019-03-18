def is_prime(n):
    if n >= 2:
        for y in range(2, n):
            if not (n % y):
                return False
    else:
        return False
    return True


def primes(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes
