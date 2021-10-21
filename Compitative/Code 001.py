# import math

a = []
n = int(input("Enter the no. of elements = "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)
i = 0
while True:
    if max(a) == 0:
        break
    if (a.index(max(a)) - 1) >= 0 or a[a.index(max(a)) - 1] != 0:
        a[a.index(max(a)) - 1] = 0
    a[a.index(max(a))] = 0
    i += 1
print(i)
