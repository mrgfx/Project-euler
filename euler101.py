from fractions import Fraction
from functools import reduce
import operator

# the true sequence U(n)
def U(n):
    return sum((-1)**i * n**i for i in range(11))   # i = 0 … 10

def lagrange_fit(k):
    """return P_k(k+1) as an integer (exact rational arithmetic)"""
    # points (i, U(i)) for i = 1..k
    pts = [(i, U(i)) for i in range(1, k+1)]

    # compute P_k(k+1) using Lagrange formula
    x = k + 1
    total = Fraction(0, 1)
    for i, yi in pts:
        # basis polynomial ℓ_i(x)
        num = Fraction(1, 1)
        den = Fraction(1, 1)
        for j, _ in pts:
            if j == i: continue
            num *= (x - j)
            den *= (i - j)
        total += yi * num / den
    return total   # exact rational, will be integer for this problem

fit_sum = 0
for k in range(1, 11):
    fit = lagrange_fit(k)
    if fit != U(k+1):          # BOP → FIT
        fit_sum += fit

print(fit_sum)   # → 37076114526
