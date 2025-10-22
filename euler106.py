import itertools
from math import comb

def needs_testing(a, b):
    """Check if a and b interleave (i.e., neither is always greater than the other)."""
    greater = less = 0
    for x, y in zip(a, b):
        if x > y:
            greater += 1
        elif x < y:
            less += 1
    # If all elements of one are strictly greater, we can skip testing
    return greater > 0 and less > 0

def count_tests(n):
    total_tests = 0
    elements = list(range(n))
    for k in range(2, n // 2 + 1):
        combos = list(itertools.combinations(elements, 2 * k))
        for combo in combos:
            all_k_subsets = list(itertools.combinations(combo, k))
            seen = set()
            for i in range(len(all_k_subsets)):
                A = all_k_subsets[i]
                setA = set(A)
                for j in range(i + 1, len(all_k_subsets)):
                    B = all_k_subsets[j]
                    if setA.isdisjoint(B):
                        # Sort both to get deterministic comparison
                        a_sorted = sorted(A)
                        b_sorted = sorted(B)
                        if needs_testing(a_sorted, b_sorted):
                            total_tests += 1
    return total_tests

print("Number of subset pairs to test for n = 12:", count_tests(12))
