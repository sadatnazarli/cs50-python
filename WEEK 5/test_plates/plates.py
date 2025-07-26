def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (check_length(s) and
            check_start_letters(s) and
            check_numbers_end(s) and
            check_first_number(s) and
            check_alphanumeric(s))


def check_length(s):
    return 2 <= len(s) <= 6


def check_start_letters(s):
    return len(s) >= 2 and s[:2].isalpha()


def check_numbers_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i:].isdigit()
    return True


def check_first_number(s):
    for char in s:
        if char.isdigit():
            return char != '0'
    return True


def check_alphanumeric(s):
    return s.isalnum()


if __name__ == "__main__":
    main()
