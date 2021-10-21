# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def prnt_rangoli(num):
    dsh = num - 1
    alp = num
    num = num + num
    for i in range(1, num):
        print(i)
        # pass
    print(dsh * '-')


prnt_rangoli(int(input()))

# def prnt_s(num):
#     return ''
#
#
# def print_rangoli(size):
#     s = size
#     dash = int(((size * 2) - 1) + ((size * 2) - 2))
#     size = 96 + size
#     dash = int(dash / 2)
#     for i in range(1, (s * 2)):
#         print('-' * dash + prnt_s(i) + '-' * dash)
#         dash = dash - 2
#
#
# n = int(input())
# print_rangoli(n)
