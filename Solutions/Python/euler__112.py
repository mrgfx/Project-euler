def is_bouncy(n):
    s = str(n)
    inc = False
    dec = False
    for i in range(len(s)-1):
        if s[i+1] > s[i]:
            inc = True
        elif s[i+1] < s[i]:
            dec = True
        if inc and dec:
            return True
    return False

# Initialize count: below 100 there are no bouncy numbers
bouncy_count = 0
n = 99

# Increment n until the bouncy ratio is exactly 99%
while True:
    n += 1
    if is_bouncy(n):
        bouncy_count += 1
    # Check if 100 * bouncy_count == 99 * n
    if bouncy_count * 100 == 99 * n:
        print("Least n with 99% bouncy:", n)
        break
