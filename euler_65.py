from fractions import Fraction

def continued_fraction_e(n):
    # Build the continued fraction sequence for e
    terms = [2]
    k = 1
    while len(terms) < n:
        terms += [1, 2 * k, 1]
        k += 1
    return terms[:n]

def compute_convergent(terms):
    # Start from the end and work backwards using recurrence
    frac = Fraction(terms[-1])
    for term in reversed(terms[:-1]):
        frac = term + 1 / frac
    return frac

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Main execution
terms = continued_fraction_e(100)
convergent = compute_convergent(terms)
result = sum_of_digits(convergent.numerator)

print("Sum of digits in the numerator of the 100th convergent of e:", result)
