n, m, v = map(int, input().split())
graph = []
visited = [False] * m

for i in range(m):
    graph.append(list(map(int, input().split())))


def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 인접한 다른 노드를 재귀적으로 방문하기
    for i in graph[v]:
        print(i)
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, v, visited)
