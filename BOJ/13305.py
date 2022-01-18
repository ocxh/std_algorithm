n = int(input())  # 도시 수
lag = list(map(int, input().split()))  # 다리 길이
an = list(map(int, input().split()))  # 도시별 주유소 비용

cost = an[0] * lag[0]  # 초기 비용(확정)
now = an[0]  # 현재위치
count = 1  # 다음칸의 초기 인덱스

while count < n - 1:
    if now > an[count]:
        now = an[count]
    cost += now * lag[count]
    count += 1

print(cost)
