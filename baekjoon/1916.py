import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        now, dis = heapq.heappop(q)
        if distance[now] < dis:
            continue

        for i in graph[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))


dijkstra(start)
print(distance[end])
