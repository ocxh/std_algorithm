import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())

arr = [[] for _ in range(200002)]
for i in range(100001):
    arr[i].append((i * 2, 0))
    arr[i].append((i + 1, 1))
    arr[i].append((i - 1, 1))


def dijkstra(start, end):
    time = [INF] * (200002)
    q = []
    q.append((0, start))
    time[start] = 0

    while q:
        t, now = heapq.heappop(q)
        if time[now] < t:
            continue

        for i in arr[now]:
            cost = i[1] + t
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return time[end]


print(dijkstra(n, k))
