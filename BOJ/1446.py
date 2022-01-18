import sys

input = sys.stdin.readline

n, d = map(int, input().split())
arr = [[] for i in range(10000 + 1)]  # 지름길의 위치 저장

for i in range(n):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))  # a부터 b까지 가는 길이가 c인 지름길

count = [i for i in range(10000 + 1)]  # 전체 구간의 비용

for i in range(0, d + 1):
    if i != 0:
        count[i] = min(count[i], count[i - 1] + 1)  # 현재 구간의 비용 = 현재 구간과 (이전구간)+1 중 작은것

    if len(arr[i]) > 0:  # 현재 위치에 해당하는 지름길이 있다면
        for nb, nc in arr[i]:  # 목적지 nb와 비용 nc를 추출
            cost = nc + count[i]  # 목적지의 비용 = 현재까지의 비용+nc(지름길을 통한 비용)

            if count[nb] > cost:  # 만약 목적지의 기존비용보다 지름길을 통한 비용이 더 작으면
                count[nb] = cost


print(count[d])
