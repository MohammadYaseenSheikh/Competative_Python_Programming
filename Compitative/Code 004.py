# A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
# For example, according to the conditions described above,
#  would have it's logo with the letters .
# Input Format
# A single line of input containing the string .
# Constraints
#  has at least  distinct characters
# Output Format
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
# link: https://www.hackerrank.com/challenges/most-commons/problem
# Sample Input 0
# aabbbccde
# Sample Output 0
# b 3
# a 2
# c 2

import math
import os
import random
import re
import sys

# s = input()
s = "aabbbccde"
next_a = 97
chk = chr(next_a)
cnt = 0
alp = []
s = sorted(s)
n = len(s)
pt = 0
i = 1
while next_a <= 122:
    l = True
    while l and pt < n:
        if chk == s[pt]:
            cnt += 1
            pt += 1
        else:
            l = False
    alp.append(cnt)
    cnt = 0
    next_a += 1
    chk = chr(next_a)
    if pt >= n : break
for i in range(3):
    chk = chr(alp.index(max(alp)) + 97)
    print(chk, end=" ")
    print(max(alp))
    alp[alp.index(max(alp))] = 0