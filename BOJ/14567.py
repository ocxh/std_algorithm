from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
res = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def tp_sort():
    result = 1
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 1))
            res[i] = 1

    while q:
        now, result = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, result + 1))
                res[i] = result + 1


tp_sort()
for i in range(1, n + 1):
    print(res[i], end=" ")
