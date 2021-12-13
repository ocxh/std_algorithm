# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1

result = [0, 0]
ans = 2e9 + 1
while start < end:
    total = arr[start] + arr[end]

    if abs(total) < ans:
        ans = abs(total)
        result[0], result[1] = arr[start], arr[end]

    if total < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])
