import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))


def dijkstra(start, end):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]


res = 0
for i in range(1, n + 1):
    res = max(res, dijkstra(i, x) + dijkstra(x, i))

print(res)
