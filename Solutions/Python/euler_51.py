from itertools import combinations, product

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit:i] = [False] * len(range(i*i, limit, i))
    return [i for i, prime in enumerate(sieve) if prime]

def prime_digit_replacements(primes, family_size=8):
    for p in primes:
        s = str(p)
        n_digits = len(s)
        # Check all non-empty combinations of digit positions
        for r in range(1, n_digits):
            for positions in combinations(range(n_digits), r):
                primes_found = []
                # Replace chosen positions with digits 0-9
                for digit in '0123456789':
                    # Skip if replacement makes number start with 0
                    if positions[0] == 0 and digit == '0':
                        continue
                    new_s = list(s)
                    for pos in positions:
                        new_s[pos] = digit
                    candidate = int(''.join(new_s))
                    if candidate in primes_set:
                        primes_found.append(candidate)
                if len(primes_found) == family_size:
                    return min(primes_found)
    return None

if __name__ == "__main__":
    limit = 1_000_000
    primes = generate_primes(limit)
    primes_set = set(primes)
    result = prime_digit_replacements(primes, family_size=8)
    print(f"The smallest prime in an eight prime value family is {result}.")
