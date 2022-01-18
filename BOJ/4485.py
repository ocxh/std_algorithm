import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
while True:
    count += 1
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    visited = [[False] * n for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    distance[0][0] = 0
    visited[0][0] = True

    while q:
        dist, x, y = heapq.heappop(q)
        if x != 0 and y != 0:
            if distance[y][x] < dist:
                continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[ny][nx]
                if distance[ny][nx] > cost:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print("Problem %d: %d" % (count, distance[n - 1][n - 1]))
