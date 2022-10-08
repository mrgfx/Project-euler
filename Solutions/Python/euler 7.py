from math import sqrt, ceil

def nthPrime(n):
    primes = [2]
    i=1
    while len(primes) < n:
        current = primes[-1] + i
        isPrime = True
        for x in range(2,ceil(sqrt(current)+1)):
            if current % x == 0:
                isPrime = False
        if isPrime == True:
            primes += current,
            i=1
        else:
            i+=1
    return primes[-1]
            
   
print(nthPrime(10001))
