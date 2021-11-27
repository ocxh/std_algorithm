from collections import deque


def bfs(x, y):
    que.append((x, y))
    visited[y][x] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                que.append((nx, ny))
                visited[ny][nx] = True


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]
    que = deque()

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1 and not visited[j][i]:
                bfs(i, j)
                count += 1
    result.append(count)
for res in result:
    print(res)
