from collections import deque

coms = int(input())
n = int(input())

graph = [[] for i in range(coms + 1)]
visited = [False] * (coms + 1)

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v, graph, visited):
    visited[v] = True
    q = deque([v])
    while q:
        bf = q.popleft()
        for i in graph[bf]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True


bfs(1, graph, visited)
print(visited.count(True) - 1)
