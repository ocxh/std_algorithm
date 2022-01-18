#4.미로탈출 문제 풀이
from collections import deque

def bfs(x, y):
    #큐 생성
    queue = deque()
    queue.append((x, y))
    #큐가 없어질 때 까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로 위치확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위에 벗어난 값 무시
            if nx<0 or nx >=n or ny<0 or ny >=m:
                continue
            # 벽 무시
            if graph[nx][ny] == 0:
                continue
            #처음 방문하는 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    #가장 오른쪽 아래까지 최단거리 반환
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))