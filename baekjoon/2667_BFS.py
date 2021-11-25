from collections import deque

n = int(input())
graph = list()
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

all_count = list()
q = deque()


def bfs(x, y):
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] != 1:
                continue
            q.append((nx, ny))
            graph[nx][ny] = 0
            buffer.append(1)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            buffer = []
            bfs(i, j)
            all_count.append(sum(buffer) + 1)


all_count.sort()
print(len(all_count))
for i in all_count:
    print(i)
