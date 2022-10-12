def sum_of_divisors(n):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum


if __name__ == '__main__':
    amicable_numbers = []
    for i in range(1, 10001):
        b = sum_of_divisors(i)
        if sum_of_divisors(b) == i and b != i:
            amicable_numbers.append(i)
            amicable_numbers.append(b)
    amicable_list = [*set(amicable_numbers)]
    sum_amicable_numbers = sum(amicable_list)
    print(sum_amicable_numbers)
