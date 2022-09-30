calc = 0
highest = 0

def isPalindrome(x,a,b):
    global highest
    if str(x) == str(x)[::-1]:
        if x > highest:
            highest = calc
        print(a,' * ',b,' = ',x)

for x in range(1000,100,-1):
    for y in range(1000,100,-1):
        calc = x*y
        isPalindrome(calc,x,y)
    
print(highest)
