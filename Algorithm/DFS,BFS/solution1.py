#3.음료수 얼려 먹기 문제

def dfs(x, y):
    #범위에 벗어난 값일경우 종료
    if x <= -1 or x >=n or y <= -1 or y >=m:
        return False
    
    #현재 노드가 방문처리 안된 노드라면 상하좌우 모두 방문처리
    if graph[x][y]==0:
        #해당노드 방문처리
        graph[x][y]=1
        #상하좌우 방문처리
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result+=1

print(result)