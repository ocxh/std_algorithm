import sys

sys.setrecursionlimit(100000)
m, n, k = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(k)]
visited = [[False] * n for i in range(m)]

result = []
buffer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for a in range(k):
    x1 = arr[a][0]
    x2 = arr[a][2]
    y1 = arr[a][1]
    y2 = arr[a][3]

    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = True


def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if visited[ny][nx] == False:
            dfs(nx, ny)
            buffer.append(1)


for i in range(n):
    for j in range(m):
        if visited[j][i] == False:
            buffer = []
            dfs(i, j)
            result.append(sum(buffer) + 1)

print(len(result))
result.sort()
for i in result:
    print(i, end=" ")
