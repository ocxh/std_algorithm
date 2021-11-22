from collections import deque

# 게임판의 크기 입력 받기
n = int(input())

# 게임판 요소들 입력받기
graph = [list(map(int, input().split())) for _ in range(n)]

# 게임판 방문처리
visit = [[False] * n for _ in range(n)]

# 이동 가능 거리
dx = [1, 0]
dy = [0, 1]

queue = deque()


def bfs(x, y):
    queue.append((x, y))
    visit[x][y] = True
    # queue에 값이 있으면
    while queue:
        # q에서 x, y값을 빼옴
        x, y = queue.popleft()
        # 현재 위치가 목적지이면 성공메세지 return
        if graph[x][y] == -1:
            return "HaruHaru"
        # 현재 위치가 목적지가 아닐경우(오른쪽 이동과 아래 이동 총 2가지 경우)
        for i in range(2):
            # 이동 가능 거리만큼 이동후 x,y 좌표
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            # 이동한 위치가 게임판을 벗어나면 x
            # 이동한 위치가 이미 방문한 곳이면 x

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] == True:
                continue
            visit[nx][ny] = True
            queue.append((nx, ny))
    # 실패 메세지 return
    return "Hing"


print(bfs(0, 0))
