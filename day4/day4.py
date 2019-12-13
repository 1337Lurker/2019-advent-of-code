def main():
    valid_numbers = []
    for number in range(271973, 785962):
        if has_two_adjacent_digits(number) and has_only_decreasing_digits(number):
            valid_numbers.append(number)
    print(len(valid_numbers))


def has_two_adjacent_digits(number):
    number = str(number)
    valid = False
    for i in range(0, 5):
        if number[i] == number[i + 1]:
            valid = True
    return valid


def has_only_decreasing_digits(number):
    number = str(number)
    valid = True
    for i in range(0, 5):
        if number[i] > number[i+1]:
            valid = False
    return valid


if __name__ == "__main__":
    # execute only if run as a script
    main()
