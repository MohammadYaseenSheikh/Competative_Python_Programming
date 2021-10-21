s = "1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
str1 = True
str2 = False
str3 = False
str4 = False
str5 = False

for i in range(0, len(s)):
    if s[i].isdigit():
        str3 = True
        continue
    if not s[i].isalnum():
        str1 = False
        continue
    if str2 == str4 == str5 == True:
        continue
    if s[i].islower():
        str2 = True
        str4 = True
    else:
        str5 = True
        str2 = True
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

# str1 = True
# str2 = False
# str3 = False
# str4 = False
# str5 = False
#
# for i in range(0, len(s)):
#     if s[i].isdigit():
#         str3 = True
#         continue
#     if str2 == str4 == str5 == True:
#         continue
#     if s[i].islower():
#         str2 = True
#         str4 = True
#     else:
#         str5 = True
#         str2 = True
#     if str1:
#         str1 = s[i].isalnum()
#         continue
#
#
# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)