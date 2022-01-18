import sys
from collections import deque


def bfs(start):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in arr[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return visited.count(True)


n, m = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    A, B = map(int, sys.stdin.readline().split())
    arr[B].append(A)

res = [0] * (n + 1)
for i in range(1, n + 1):
    res[i] = bfs(i)

for i in range(1, n + 1):
    if max(res) == res[i]:
        print(i, end=" ")
