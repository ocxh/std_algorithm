# 그리디 큰 수의 법칙
# 나의 코드
# 자칫하면 시간초과 받기 쉬운 방식
"""
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

max = arr[n-1]
sec = arr[n-2]

result = 0
for x in range(1, m+1):
        if x % k !=0:
            result += max
        else:
            result += sec

print(result)
"""
# 나동빈님 코드
# m의 개수가 늘어나도 시간 초과가 발생되지 않는 방식
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
#k+1을 m으로 나눈 후 = 반복되는 구간 개수
# * k를 하게되면 반복되는 구간에서 큰 수가 더해지는 횟수가 나온다
count += m%(k+1)
#반복구간 밖에서 더해지는 가장 큰 값의 개수

result=0
result += count*first # 가장 큰 수 더하기
result += (m-count) * second # 두번쨰로 큰 수 더하기

print(result)


