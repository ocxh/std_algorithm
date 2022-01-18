import sys

sys.setrecursionlimit(100000)
n = int(input())

graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
num_RGB = 0
num_ALL = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, c1, c2):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        if visited[ny][nx] == False and (c1 == graph[ny][nx] or c2 == graph[ny][nx]):
            dfs(nx, ny, c1, c2)


for i in range(n):
    for j in range(n):
        if (graph[i][j] == "R" or graph[i][j] == "G") and visited[i][j] == False:
            dfs(j, i, "R", "G")
            num_RGB += 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == "B" and visited[i][j] == False:
            dfs(j, i, "B", "")
            num_RGB += 1
visited = [[False] * n for _ in range(n)]
colors = ["R", "G", "B"]
for t in colors:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == t and not visited[i][j]:
                dfs(j, i, t, "")
                num_ALL += 1

print(num_ALL, num_RGB)
