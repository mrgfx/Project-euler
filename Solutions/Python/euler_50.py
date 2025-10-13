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

def prime_sieve(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit:i] = [False] * len(range(i*i, limit, i))
    return [i for i, prime in enumerate(sieve) if prime]

def longest_prime_sum(limit):
    primes = prime_sieve(limit)
    prime_set = set(primes)

    max_length = 0
    max_prime = 0

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            total = sum(primes[i:j])
            if total > limit:
                break
            if total in prime_set:
                if j - i > max_length:
                    max_length = j - i
                    max_prime = total

    return max_prime, max_length

if __name__ == "__main__":
    limit = 1_000_000
    prime, length = longest_prime_sum(limit)
    print(f"The prime below {limit} that can be written as the sum of the most consecutive primes is {prime}.")
    print(f"It is the sum of {length} consecutive primes.")
