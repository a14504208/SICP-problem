from math import sqrt
from random import randint

def smallest_divisor(n):
    """
    Return the smallest divisor of n
    """
    
    sqrt_n = round(sqrt(n))

    def next_to(n):
        a = 2
        while a <= n:
            yield a
            if a == 2:
                a = 3
            else:
                a += 2
    
    for i in next_to(sqrt_n + 1):
        if n % i == 0:
            return i

    return n
    
def is_prime(n):
    if n == 1:
        return False
    else:
        return n == smallest_divisor(n)

def expmod(base, exp, m):
    """
    Return the remainder of base raised to exp modulo m
    """
    remain = 1
    
    while True:
        if exp == 0:
            return remain
        elif exp % 2 == 0:
            base = (base * base) % m
            exp = exp // 2
        else:
            exp -= 1
            remain = (remain * base) % m

def fermat_test(n, time = 10):
    """
    Test if n is prime based on Fermat test n times
    """

    for _ in range(time):
        a = randint(2, n - 1)
        if not expmod(a, n, n) == a:
            return False

    # After passing enough time of Fermat test
    return True

def fermat_test_all(n):
    """
    Test if n pass all Fermat test for every a < n
    """
    for i in range(2, n):
        if not expmod(i, n, n) == i:
            return False

    return True
