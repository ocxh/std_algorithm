import sys

input = sys.stdin.readline
INF = int(1e9)

a, b = input().split()
dif = len(b) - len(a)

res = INF
for i in range(dif + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            cnt += 1
    res = min(res, cnt)

print(res)
