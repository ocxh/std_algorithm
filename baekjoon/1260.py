from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]  # 그래프 초기화
visited = [False] * (n + 1)  # 방문처리 초기화

# 노드 graph만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드에 연결된 간선 정렬
for i in range(1, n + 1):
    graph[i].sort()

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] != True:
            dfs(graph, i, visited)


# bfs
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
print()
visited = [False] * (n + 1)  # 방문처리 초기화
bfs(graph, v, visited)
