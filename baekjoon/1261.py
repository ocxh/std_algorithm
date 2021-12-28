from collections import deque

INF = int(1e9)
m, n = map(int, input().split())  # 가로 세로 길이
arr = [list(map(int, input())) for _ in range(n)]  # 방과 벽
brk = [[INF] * m for _ in range(n)]  # 최소 부순 벽 개수
visited = [[False] * m for _ in range(n)]  # 방문지

# 이동거리
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
q = deque()
q.append((0, 0))
visited[0][0] = True
brk[0][0] = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            if arr[ny][nx] == 1:
                cost = brk[y][x] + 1
                q.append((nx, ny))
            else:
                cost = brk[y][x]
                q.appendleft((nx, ny))  # 해당 부분이 핵심. 비용이 적은 부분을 우선적으로 탐색

            if brk[ny][nx] > cost:
                brk[ny][nx] = cost


print(brk[n - 1][m - 1])
