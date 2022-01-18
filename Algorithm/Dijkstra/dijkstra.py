import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수/ 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용c
    graph[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # q가 비어있지 않으면
        # 거리와 현재노드를 q에서 꺼냄
        dist, now = heapq.heappop(q)
        # 최단거리 테이블에서 현재 노드의 거리가 dist보다 짧으면 반복문으로
        if distance[now] < dist:
            continue
        for i in graph[now]:  # 현재 노드와 연결된 다른 노드들 확인
            cost = dist + i[1]  # 지금까지의 거리 dist + now에서 i[0]노드까지의 거리 i[1]

            if cost < distance[i[0]]:  # 만약 현재 측정 비용이 최단거리 테이블 거리보다 짧으면
                distance[i[0]] = cost  # 최단거리 테이블 재설정
                heapq.heappush(q, (cost, i[0]))  # 힙에 넣는다(현재 노드와 비용을)


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
