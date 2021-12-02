n = int(input())
k = int(input())
answer = 0

start = 1
end = k  # k번째 수는 k보다 클 수가 없음


while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)  # mid 이하의 수가 몇개인지

    if count >= k:  # count가 k보다 커도 중복숫자이기에
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
