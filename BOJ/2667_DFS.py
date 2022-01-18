n = int(input())

graph = list()
for i in range(n):
    graph.append(list(map(int, input())))

all_count = list()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, buffer):
    if x >= n or x < 0 or y >= n or y < 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        buffer.append(1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, buffer)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            buffer = []
            dfs(i, j, buffer)
            all_count.append(sum(buffer))


all_count.sort()
print(len(all_count))
for i in all_count:
    print(i)
