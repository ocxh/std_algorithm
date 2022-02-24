import sys

sys.setrecursionlimit(10 ** 9)

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
table = [-1 for _ in range(n + 1)]
table[b] = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start):
    now = table[start] + 1
    for i in graph[start]:
        if visited[i] == False:
            table[i] = now
            visited[i] = True
            dfs(i)


dfs(b)
if a == b:
    print(0)
else:
    print(table[a])
