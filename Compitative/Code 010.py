# https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())
Nested_list = []

# Taking input
for i in range(n):
    a = input()
    b = float(input())
    Nested_list.append([b, a])

Nested_list.sort()
min_v = Nested_list[0][0]

while True:
    if min_v == Nested_list[0][0] and n > 1:
        del Nested_list[0]
        n = len(Nested_list)
    else:
        break

min_v = Nested_list[0][0]
fnl_list = []

for i in range(n):
    if min_v == Nested_list[i][0]:
        fnl_list.append(Nested_list[i][1])
    else:
        break

fnl_list.sort()

for i in range(len(fnl_list)):
    print(fnl_list[i])

# for i in range(1, len(Nested_list)):
#     if min_1 > Nested_list[i][1]:
#         min_1 = Nested_list[i][1]
# scnd_sml = []
# for i in range(n):
#     if min_1 == Nested_list[i][1]:
#         scnd_sml.append(Nested_list[i][0])
# scnd_sml.sort()
# print(scnd_sml)




# min_i1 = 0
# Nested_list.sort()
# min_i2 = 0
# min_2 = -1
# diff = 0
#
# if n == 2:
#     print(Nested_list[0][0])
#     print(Nested_list[1][0])
#     exit()
#
# min_1 = Nested_list[0][1]
# for i in range(1, n):
#     if min_1 > Nested_list[i][1]:
#         min_1 = Nested_list[i][1]
#
# diff = Nested_list[0][1] - min_1
# diff1 = Nested_list[1][1] - min_1
# diff3 = 0.0
# i1 = 0
# i2 = 1
# for i in range(2, n):
#     diff3 = Nested_list[i][1] - min_1
#     if diff >= diff3 and min_1 != Nested_list[i][1]:
#         if diff3 >= diff1:
#             diff = diff3
#             i1 = i
#         else:
#             diff1 = diff3
#             i2 = i
#
#         i1 = i
#     diff1 = Nested_list[i][1] - min_1
# if Nested_list[i1][0] < Nested_list[i2][0]:
#     print(Nested_list[i1][0])
#     print(Nested_list[i2][0])
# else:
#     print(Nested_list[i2][0])
#     print(Nested_list[i1][0])




# n = int(input())
# str = []
# scr = []
# str_f = []
# for i in range(n):
#     str.append(input())
#     scr.append(float(input()))
# scr_t = scr
# scr_t.sort()
# cnt = 0
# i = 1
# while cnt < 2:
#     j = 0
#     while j < n:
#         if scr_t[i] == scr[j]:
#             scr[j] = -1
#             str_f.append(str[j])
#             cnt += 1
#             i += 1
#             break
#         j += 1
# print(str_f.sort())

# std = []
# fl = 1000000
# sl = []
# l = False
# i = 0
# i_fl = 0
# for i in range(int(input())):
#         name = input()
#         score = float(input())
#         std.append([name, score])
#
#         if i == 0:
#             fl = std[i][1]
#             i_fl = i
#             continue
#         if fl > std[i][1]:
#             fl = std[i][1]
#             sl.clear()
#             sl.append(i_fl)
#             i_fl = i
#             continue
#         sl.append(i)
#
# i = 0
# while i < len(sl):
#     print(std[sl[i]][0])
#     i += 1
