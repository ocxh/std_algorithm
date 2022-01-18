import sys

sys.setrecursionlimit(10 ** 9)

n = int(input())

arr = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)
p = [0] * (n + 1)


def dfs(v, visited, arr):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            p[i] = v
            dfs(i, visited, arr)


dfs(1, visited, arr)
for i in range(2, n + 1):
    print(p[i])
