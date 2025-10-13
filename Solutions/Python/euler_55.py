def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n, max_iter=50):
    num = n
    for _ in range(max_iter):
        num += int(str(num)[::-1])
        if is_palindrome(num):
            return False  # Not a Lychrel number
    return True  # Lychrel number

count = 0
for n in range(1, 10_000):
    if is_lychrel(n):
        count += 1

print(f"There are {count} Lychrel numbers below 10,000.")
