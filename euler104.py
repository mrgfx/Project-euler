import math

def is_pandigital_1_to_9(n):
    return sorted(str(n)) == ['1','2','3','4','5','6','7','8','9']

def first_nine_digits(n):
    # Using logarithmic approximation
    phi = (1 + math.sqrt(5)) / 2
    log_fib_n = n * math.log10(phi) - math.log10(math.sqrt(5))
    decimal_part = log_fib_n - int(log_fib_n)
    first_9 = int(10**(decimal_part + 8))  # 10^(x) gives us first 9 digits
    return first_9

def find_pandigital_fib_index():
    mod = 10**9
    a, b = 1, 1
    index = 2
    while True:
        a, b = b, (a + b) % mod
        index += 1

        if is_pandigital_1_to_9(b):
            first9 = first_nine_digits(index)
            if is_pandigital_1_to_9(first9):
                return index

# Solve the problem
print(find_pandigital_fib_index())
