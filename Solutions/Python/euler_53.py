import math

count = 0
limit = 1_000_000

for n in range(1, 101):
    for r in range(0, n + 1):
        if math.comb(n, r) > limit:
            count += 1

print(f"The number of values of nCr greater than one million is {count}.")
