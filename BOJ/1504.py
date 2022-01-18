import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))  # 목적지, 거리
    arr[b].append((a, c))  # 목적지, 거리
v1, v2 = map(int, input().split())


def dijkstra(start, end):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))  # 경로와 시작 위치
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]


result = min(
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n),
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n),
)

if result >= INF:
    print(-1)
else:
    print(result)
