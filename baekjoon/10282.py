import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dis[now] < cost:
            continue

        for i in graph[now]:
            if cost + i[1] < dis[i[0]]:
                dis[i[0]] = cost + i[1]
                heapq.heappush(q, (cost + i[1], i[0]))


t = int(input())  # 테스트 케이스 수
for _ in range(t):
    n, d, start = map(int, input().split())  # 노드개수, 간선개수, 시작노드
    graph = [[] for _ in range(n + 1)]
    dis = [INF] * (n + 1)

    for _ in range(d):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))

    dijkstra(start)

    total = 0
    max_c = -1

    for i in range(1, n + 1):
        if dis[i] != INF:
            total += 1
            if dis[i] > max_c:
                max_c = dis[i]

    print(total, max_c)
