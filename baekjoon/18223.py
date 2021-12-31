import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]


distance = [INF] * (v + 1)
res1 = dijkstra(1, v)
distance = [INF] * (v + 1)
res2 = dijkstra(1, p)
res3 = dijkstra(p, v)

if res1 == res2 + res3:
    print("SAVE HIM")
else:
    print("GOOD BYE")
