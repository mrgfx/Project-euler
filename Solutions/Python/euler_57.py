def count_large_numerators(limit=1000):
    numerator = 3  # first expansion numerator
    denominator = 2  # first expansion denominator
    count = 0

    for _ in range(1, limit):
        # Check if numerator has more digits than denominator
        if len(str(numerator)) > len(str(denominator)):
            count += 1
        # Compute next expansion
        numerator, denominator = numerator + 2 * denominator, numerator + denominator

    return count

result = count_large_numerators()
print(f"In the first 1000 expansions, {result} fractions have a numerator with more digits than the denominator.")
