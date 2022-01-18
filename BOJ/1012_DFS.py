import sys

sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(y, x):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue
        if graph[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx)


result = []
t = int(input())
for case in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    visited = [[False] * m for i in range(n)]

    count = 0
    for i in range(m):
        for j in range(n):
            if not visited[j][i] and graph[j][i] == 1:
                dfs(j, i)
                count += 1

    result.append(count)

for i in result:
    print(i)
