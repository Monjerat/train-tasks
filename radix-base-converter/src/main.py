import sys


def char_position(letter):
    return ord(letter.casefold()) - 97


def base_check(base):
    # если основание - не целое число, вызываем исключение
    if not base.isnumeric():
        raise ValueError
    base = int(base)
    # если основание не вписывается в заданный промежуток, вызываем исключение
    if base <= 1 or base > 36:
        raise ValueError
    return base


def convert_radix_digit_to_int(radix_digit, base):
    try:
        if radix_digit.isdigit():
            int_digit = int(radix_digit)
        elif radix_digit.isalpha():
            int_digit = char_position(radix_digit) + 10
        else:
            raise ValueError

        if int_digit >= base:
            raise ValueError
        return int_digit
    except ValueError:
        print("Число не соответствует системе счисления.")
        sys.exit(1)


def partial_convert_to_decimal(base, radix_num, is_int):
    part_decimal_num = 0
    if is_int:
        first_digit_index = len(radix_num)
    else:
        first_digit_index = 0
    for idx, digit in enumerate(radix_num):
        part_decimal_num += pow(base, first_digit_index - idx - 1) * convert_radix_digit_to_int(digit, base)
    return part_decimal_num


def convert_to_decimal(base, radix_num):
    is_negative = False
    if radix_num[0] == "-":
        radix_num = radix_num[1:]
        is_negative = True
    if "." in radix_num:
        int_radix_num, frac_radix_num = radix_num.split(sep=".")
        decimal_num = partial_convert_to_decimal(base, int_radix_num, is_int=True) + \
                      partial_convert_to_decimal(base, frac_radix_num, is_int=False)
    else:
        decimal_num = partial_convert_to_decimal(base, radix_num, is_int=True)
    if is_negative:
        decimal_num = -decimal_num
    return decimal_num


if __name__ == '__main__':
    try:
        radix_base = input("Введите основание системы счисления (>1 и <=36): ")
        radix_base = base_check(radix_base)
    except ValueError:
        print("Основание должно быть целым числом >1 и <= 36.")
        sys.exit(1)

    radix_number = input("Введите число: ")
    decimal_number = convert_to_decimal(radix_base, radix_number)
    print(f"Число в десятеричной системе счисления: {decimal_number}")
