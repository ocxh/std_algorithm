# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, k = 5, 17
time = [INF] * (200002)
arr = [[] for _ in range(200002)]
for i in range(100001):
    arr[i].append((i * 2, 0))
    arr[i].append((i + 1, 1))
    arr[i].append((i - 1, 1))


def dijkstra(start, end):

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
        if now == k:
            return time[end]

    return time[end]


print(dijkstra(n, k))
for i in range(n, k + 2):
    print(i, time[i])
