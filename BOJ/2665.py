import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
arr = [[INF] * n for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))


def dijkstra(x, y):
    q = []
    arr[y][x] = 0
    heapq.heappush(q, (-arr[y][x], x, y))

    while q:
        dist, x, y = heapq.heappop(q)
        dist *= -1

        if x != 0 and y != 0:
            if arr[y][x] < dist:
                continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 0:
                    cost = dist + 1
                else:
                    cost = dist

                if arr[ny][nx] > cost:
                    arr[ny][nx] = cost
                    heapq.heappush(q, (-cost, nx, ny))
    return arr[n - 1][n - 1]


print(dijkstra(0, 0))
