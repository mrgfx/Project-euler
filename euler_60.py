import sympy

# Function to check if concatenating two numbers forms a prime
def is_prime_concatenation(p1, p2):
    # Concatenate p1 and p2 in both orders and check if both are primes
    p1p2 = int(str(p1) + str(p2))
    p2p1 = int(str(p2) + str(p1))
    return sympy.isprime(p1p2) and sympy.isprime(p2p1)

# Generate list of primes using sympy
def generate_primes(limit):
    return list(sympy.primerange(2, limit))

# Function to find the lowest sum set of 5 primes satisfying the concatenation condition
def find_lowest_prime_sum(limit=10000):
    primes = generate_primes(limit)
    
    # Backtracking function to explore valid sets of primes
    def backtrack(prime_set):
        if len(prime_set) == 5:
            return sum(prime_set)
        
        # Try adding each prime to the set and backtrack
        for prime in primes:
            if all(is_prime_concatenation(prime, p) for p in prime_set):
                prime_set.append(prime)
                result = backtrack(prime_set)
                if result:
                    return result
                prime_set.pop()
        
        return None

    # Try starting the set with an empty set
    return backtrack([])

# Call the function and print the result
result = find_lowest_prime_sum(10000)
print(f"The lowest sum for a set of 5 primes is: {result}")
