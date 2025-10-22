import math

def count_n_digit_nth_powers():
    count = 0
    n = 1
    while True:
        found = False
        for x in range(1, 10):  # x=10^n will always have more than n digits
            power = x ** n
            digits = len(str(power))
            if digits == n:
                count += 1
                found = True
        if not found:
            break  # no x^n had exactly n digits, so we can stop
        n += 1
    return count

print(count_n_digit_nth_powers())
