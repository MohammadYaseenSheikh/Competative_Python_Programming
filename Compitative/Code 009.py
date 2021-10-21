n = int(input())
arr = [2, 3, 6, 6, 5]
arr = sorted(arr)
print(arr)
i = 2
j = 1
while True:
    if arr[n-i] < arr[n-j]:
        print(arr[n-i])
        break
    i += 1
    j += 1

