import sys


def char_position(letter):
    return ord(letter.casefold()) - 97


def convert_radix_digit_to_int(radix_digit, base):
    try:
        if radix_digit.isdigit():
            int_digit = int(radix_digit)
        elif radix_digit.isalpha():
            int_digit = char_position(radix_digit) + 11
        else:
            raise ValueError

        if int_digit >= base:
            raise ValueError
        return int_digit
    except ValueError:
        print("Число не соответствует системе счисления.")
        sys.exit(1)


def convert_to_decimal(base, radix_num):
    decimal_num = 0
    number_length = len(radix_num)
    for idx, digit in enumerate(radix_num):
        decimal_num += pow(base, number_length - idx - 1) * convert_radix_digit_to_int(digit, base)
    return decimal_num


if __name__ == '__main__':
    try:
        radix_base = input("Введите основание системы счисления (>1 и <=36): ")
        # если основание - не целое число, вызываем исключение
        if not radix_base.isnumeric():
            raise ValueError
        radix_base = int(radix_base)
        # если основание не вписывается в заданный промежуток, вызываем исключение
        if radix_base <= 1 or radix_base > 36:
            raise ValueError
    except ValueError:
        print("Основание должно быть целым числом >1 и <= 36.")
        sys.exit(1)

    radix_number = input("Введите число: ")
    decimal_number = convert_to_decimal(radix_base, radix_number)
    print(f"Число в десятеричной системе счисления: {decimal_number}")
