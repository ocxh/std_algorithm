# 싸이클을 찾는 문제
import sys

sys.setrecursionlimit(10 ** 9)


def dfs(start, i):
    visited[start] = True
    now = arr[start]

    if not visited[now]:
        dfs(now, i)
    elif now == i:
        res.append(start)


n = int(input())
res = []

arr = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i] = int(input())

for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    dfs(i, i)

res.sort()
l = len(res)
print(l)
for i in range(n):
    print(res[i])
