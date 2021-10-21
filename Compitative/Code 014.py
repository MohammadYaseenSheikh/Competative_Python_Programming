def swap_case(s):
    str = ""
    for i in range(len(s)):
        if s[i].isupper():
            str += s[i].lower()
        else:
            str += s[i].upper()
    return str

s = input()
print(swap_case(s))

