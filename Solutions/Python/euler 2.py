x = 1
y = 2
calculate = 0
while x <= 4000000:
    if x%2 == 0:
        calculate += x
    x,y = y,x+y
print(calculate)
