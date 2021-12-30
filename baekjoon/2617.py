import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
arr = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    arr[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

res = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if INF > arr[i][j] > 0:
            count += 1
    if count > n // 2:
        res += 1

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if INF > arr[j][i] > 0:
            count += 1
    if count > n // 2:
        res += 1

print(res)
