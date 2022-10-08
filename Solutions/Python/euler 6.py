def sumOfSquares(n: int):
    return (n*(n+1)*(2*n+1))/(6)

def squareOfSum(n: int):
    return ((1+n)*(n/2))**2

print(int(squareOfSum(100) - sumOfSquares(100)))
