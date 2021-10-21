s = "2548963137"
s1 = ""
s2 = ""
for i in range(10):
    if i%2 == 0 or i == 0:
       s1 +=  s[i]
    else:
        s2 += s[i]
print(s1+s2)