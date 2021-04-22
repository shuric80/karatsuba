import math


def size_base10(num: int) -> int:
    return math.log10(num) + 1


def calc_karatsuba(a: int, b: int) -> int:
    if a < 10 or b < 10:
        return a * b

    m = min(size_base10(a), size_base10(b))
    m2 = math.floor(m / 2)

    a_high, a_low = a // (10**m2), a % (10**m2)
    b_high, b_low = b // (10**m2), b % (10**m2)

    z0 = calc_karatsuba(a_low, b_low)
    z1 = calc_karatsuba((a_low + a_high), (b_low + b_high))
    z2 = calc_karatsuba(a_high, b_high)

    return z2 * 10**(2 * m2) + ((z1 - z2 - z0) * 10**m2) + z0
