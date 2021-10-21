str = "aaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccdghslajkhfjksahfjkashfkjlahfjkldahfklladkf"
str = str.upper()
ltr_p = 65
chr1 = chr(ltr_p)
ind = 0
# print(chr1)
# ltr += 1
# chr1 = chr(ltr)
# print(chr1)
alp = [0]
str = sorted(str)
print(str)
for i in range(25):
    chr1 = chr(ltr_p)
    # if str[i] == chr1:
    if chr1 in str:
        ind = str.index(chr1)
        if ind == len(str):
            break
        alp.append(alp[i - 1] - ind)
        ltr_p += 1
    else:
        alp.append(0)
print(alp)
