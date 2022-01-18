from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]

count[0][0] = 1
visited[0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    if x == m and y == n:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if arr[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                count[ny][nx] += count[y][x] + 1

print(count[n - 1][m - 1])
