import math

def is_square(n):
    return int(math.isqrt(n)) ** 2 == n

def solve():
    max_x = 0
    result_D = 0

    for D in range(2, 1001):
        if is_square(D):
            continue

        m, d, a = 0, 1, int(math.isqrt(D))
        num1, num = 1, a
        den1, den = 0, 1

        while num * num - D * den * den != 1:
            m = d * a - m
            d = (D - m * m) // d
            a = (int(math.isqrt(D)) + m) // d

            num2 = num1
            num1 = num
            den2 = den1
            den1 = den

            num = a * num1 + num2
            den = a * den1 + den2

        if num > max_x:
            max_x = num
            result_D = D

    return result_D

print("The value of D ≤ 1000 that produces the largest minimal x is:", solve())
