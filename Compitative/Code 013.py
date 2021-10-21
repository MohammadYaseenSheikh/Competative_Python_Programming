# https://www.hackerrank.com/challenges/python-lists/problem
N = int(input())
a = []
str_l = []
i = 0
while i < N:
    str_l.append(input())
    i += 1
i = 0
while i <= N-1:
    str1 = str_l[i]
    if str1.find("print") != -1:
        print(a)
    if str1.find("pop") != -1:
        a.pop()
    if str1.find("sort") != -1:
        a.sort()
    if str1.find("reverse") != -1:
        a.reverse()
    if str1.find("insert") != -1:
        d = str1.split()
        a.insert(int(d[1]), int(d[2]))
    if str1.find("remove") != -1:
        d = str1.split()
        a.remove(int(d[1]))
    if str1.find("append") != -1:
        d = str1.split()
        a.append(int(d[1]))
    i += 1

