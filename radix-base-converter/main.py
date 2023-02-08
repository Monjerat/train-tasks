def convert_to_decimal(base, radix_num):
    decimal_num = 0
    number_length = len(radix_num)
    for idx, digit in enumerate(radix_num):
        decimal_num += pow(base, number_length - idx - 1) * int(digit)
    return decimal_num


if __name__ == '__main__':
    radix_base = int(input("Введите основание системы счисления (>0 и <=36): "))
    radix_number = input("Введите число: ")
    decimal_number = convert_to_decimal(radix_base, radix_number)
    print(f"Число в десятеричной системе счисления: {decimal_number}")
