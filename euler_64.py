import math

def continued_fraction_period(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return 0  # perfect square

    m, d, a = 0, 1, a0
    period = 0
    seen = set()

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        if a == 2 * a0:
            break

    return period

def count_odd_periods(limit):
    count = 0
    for n in range(2, limit + 1):
        if continued_fraction_period(n) % 2 == 1:
            count += 1
    return count

# Solve for N <= 10000
print(count_odd_periods(10000))
