def number_of_characters(n):
    UNITS_DIGITS = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    TEENS = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    TENS_DIGITS = {
        0: '',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }
    units_digit = n % 10
    tens_digit = (n // 10) % 10
    hundreds_digit = n // 100
    char_count = 0
    if hundreds_digit > 0 and hundreds_digit < 10:
        char_count += len(UNITS_DIGITS[hundreds_digit]) + 7
    elif hundreds_digit == 10:
        char_count += 11
    if tens_digit == 1:
        char_count += len(TEENS[n % 100])
        if hundreds_digit != 0:
            char_count += 3
    else:
        char_count += len(TENS_DIGITS[tens_digit]) + \
            len(UNITS_DIGITS[units_digit])
        if hundreds_digit != 0 and (tens_digit != 0 or units_digit != 0):
            char_count += 3
    return char_count


if __name__ == '__main__':
    number_of_chars = 0
    for i in range(1, 1001):
        number_of_chars += number_of_characters(i)
    print(str(number_of_chars))
