MAX_FACTOR = 20

if __name__ == '__main__':
    factors = list(range(2, MAX_FACTOR + 1))
    prod = 1
    while len(factors) > 0:
        next_factor = factors.pop(0)
        if next_factor != 1:
            prod *= next_factor
            for i in range(len(factors)):
                if factors[i] % next_factor == 0:
                    factors[i] //= next_factor
    print(prod)
