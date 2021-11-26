import sys

sys.setrecursionlimit(10000)

# 입력 받고 그래프 만들기
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리 초기화
visited = [False] * (n + 1)
buffer = [0] * (n + 1)

# dfs알고리즘
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


count = 0
# dfs실행
for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)
