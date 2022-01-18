import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

arr = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    arr[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 0:
            arr[j][i] = 0

res = [0] * (n + 1)
for i in range(1, n + 1):
    buffer = arr[i].count(INF) - 1
    print(buffer)
