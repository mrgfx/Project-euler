def same_digits(n, multiples):
    """Check if n, 2n, ..., multiples*n all have the same digits."""
    sorted_digits = sorted(str(n))
    for i in range(2, multiples + 1):
        if sorted(str(n * i)) != sorted_digits:
            return False
    return True

def find_smallest_permuted_multiple():
    n = 1
    while True:
        if same_digits(n, 6):
            return n
        n += 1

if __name__ == "__main__":
    result = find_smallest_permuted_multiple()
    print(f"The smallest positive integer x such that 2x, 3x, 4x, 5x, 6x contain the same digits is {result}.")
