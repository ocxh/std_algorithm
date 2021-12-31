import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [INF] * (n + 1)
distance = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    distance[a].append((b, c))
    distance[b].append((a, c))

q = []
start = 1
graph[start] = 0
heapq.heappush(q, (graph[start], start))

while q:
    dist, now = heapq.heappop(q)

    if dist > graph[now]:
        continue
    for i in distance[now]:
        cost = dist + i[1]
        if graph[i[0]] > cost:
            graph[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(graph[n])
