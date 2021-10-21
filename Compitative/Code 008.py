# https://www.hackerrank.com/challenges/list-comprehensions/problem
x = int(input())
y = int(input())
z = int(input())
n = int(input())

cuboid = []
cu2 = []
sm = 0
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            cuboid.append([i, j, k])

for i in range(0, len(cuboid)):
    for j in range(0, 3):
        sm = sum(cuboid[i])
    if sm != n:
        cu2.append(cuboid[i])
print(cu2)
