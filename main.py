def is_valid_binary_number(binary_number):
    return all([c in ['0', '1'] for c in binary_number])


def to_decimal(binary_number):
    inverted = binary_number[::-1]
    return sum([int(c) * (2 **idx) for (idx, c) in enumerate(inverted)])


def start():
    raw = input("Enter your binary number:\n")
    if not is_valid_binary_number(raw):
        print("The input must contains only 0's and 1's")
        return
    decimal_int = to_decimal(raw)
    print(f"Bin: {raw}\tDec: {decimal_int}")


if __name__ == "__main__":
    start()