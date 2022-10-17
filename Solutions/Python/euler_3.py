from math import sqrt, ceil

def smallestPrimeFactor(n):
    for i in range(2,ceil(sqrt(n))):
        if n % i == 0:
            return i
    return n

def main(n):
    while True:
        if n != smallestPrimeFactor(n):
            n = n / smallestPrimeFactor(n)
        else:
            return int(n)



print(main(600851475143))
