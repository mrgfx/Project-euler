import math
run = 1
a=0

while run == 1:
    for b in range(1,1001):
        c = a*a+b*b
        c = math.sqrt(c)
        if c - int(c) == 0:
            if a+b+c == 1000 and a != 0 and b != 0 and c != 0:
                run = 0
                print('Pythagorean triplet:',int(a),int(b), int(c))
                print('Answer:',int(a*b*c))
    a+=1

    
