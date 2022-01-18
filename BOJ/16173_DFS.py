# 게임판의 크기(nxn)
n = int(input())
# 게임판 맵 입력 받기
graph = list()
for i in range(n):
    graph.append(list(map(int, input().split())))

# 게임판 방문처리
visit = list()
for _ in range(n):
    visit.append([False] * n)

# 이동 가능 방향
dx = [1, 0]
dy = [0, 1]


def dfs(x, y):
    # 게임판을 벗어날경우 return
    if x >= n or x <= -1 or y >= n or y <= -1:
        return 0
    # 현재 위치가 이미 방문한곳이면 return
    if visit[x][y] == True:
        return 0
    # 목적지에 도달한 경우
    if graph[x][y] == -1:
        print("HaruHaru")
        exit()
    # 현재 위치 방문처리
    visit[x][y] = True
    # 이동 가능 거리만큼 이동 후 그 위치에서 다시 dfs
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        dfs(nx, ny)
    return 0


dfs(0, 0)
print("Hing")
