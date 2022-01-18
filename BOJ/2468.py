from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
all_count = [0]
maxh = 0
for i in range(n):
    if max(arr[i]) > maxh:
        maxh = max(arr[i])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x1, y1, h):
    q = deque()
    q.append((x1, y1))
    visited[y1][x1] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and arr[ny][nx] > h:
                    visited[ny][nx] = True
                    q.append((nx, ny))


for h in range(0, maxh):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > h:
                bfs(j, i, h)
                count += 1
    all_count.append(count)

print(max(all_count))
