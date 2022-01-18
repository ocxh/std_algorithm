from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

def bfs(graph, start, visited):
    #큐 구현
    queue = deque([start])
    #현재 노드 방문처리
    visited[start] = True
    #큐가 빌 때 까지 반복(이 부분이 탐색부분)
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        #아직 방문하지 않는 인접한 원소들을 큐에 삽입 및 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)