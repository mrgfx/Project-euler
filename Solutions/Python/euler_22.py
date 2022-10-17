if __name__ == '__main__':
    with open('p022_names.txt') as f:
        line = f.readline()
    names = line.split(',')
    names.sort()
    position = 1
    total_score = 0
    for name in names:
        real_name = name.strip("'").strip('"').strip()
        alpha_value = 0
        for i in range(len(real_name)):
            letter = real_name[i]
            ascii_value = ord(letter)
            letter_value = ascii_value - ord('A') + 1
            alpha_value += letter_value
        name_score = position * alpha_value
        total_score += name_score
        position += 1
    print(total_score)
