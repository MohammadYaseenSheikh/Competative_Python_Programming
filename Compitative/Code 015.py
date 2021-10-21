# https://www.hackerrank.com/challenges/python-string-formatting/

def print_formatted(number):
    hex_s = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        dec_ = hex_s - len(str(i))
        oct_ = hex_s - len(str(oct(i))[2:]) + 1
        hex_ = hex_s - len(str(hex(i))[2:]) + 1
        bin_ = hex_s - len(str(bin(i))[2:]) + 1
        print(dec_ * " " + str(i) + oct_ * " " + str(oct(i))[2:] + hex_ * " " + str(hex(i))[
                                                                                2:].upper() + bin_ * " " + str(bin(i))[
                                                                                                           2:])


n = int(input())
print_formatted(n)
