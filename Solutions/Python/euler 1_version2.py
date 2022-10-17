def findMultiples(multiplesOf, findBelow):
    ans = []
    for i in range(multiplesOf,findBelow, multiplesOf):
        ans += [i]
    return ans

a = findMultiples(3,1000)
b = findMultiples(5,1000)
comnineWithoutDuplicates = set(a+b)
ans = sum(comnineWithoutDuplicates)
print(ans)
