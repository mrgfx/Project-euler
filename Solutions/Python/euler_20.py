def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    fact_val = fact(100)
    digit_sum = 0
    while fact_val != 0:
        digit_sum += fact_val % 10
        fact_val //= 10
    print(digit_sum)
