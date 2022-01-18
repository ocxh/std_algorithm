import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dis = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dis[now] < cost:
            continue

        for i in graph[now]:
            if dis[i] > cost + 1:
                dis[i] = cost + 1
                heapq.heappush(q, (cost + 1, i))


dijkstra(x)

least = False
for i in range(1, n + 1):
    if dis[i] == k:
        least = True
        print(i)

if not least:
    print(-1)
