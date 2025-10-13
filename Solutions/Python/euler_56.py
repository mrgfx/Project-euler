def digit_sum(n):
    """Return the sum of digits of n."""
    return sum(int(d) for d in str(n))

max_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        s = digit_sum(a ** b)
        if s > max_sum:
            max_sum = s

print(f"The maximum digital sum of a^b for a, b < 100 is {max_sum}.")
