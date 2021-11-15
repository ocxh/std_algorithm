# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬)

n = int(input())
an = list(map(int, input().split()))
cost = int(input())

counting = sum([i for i in an])
if counting <= cost:
    print(max(an))
else:
    start = 0
    end = max(an)
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2  # 상한액
        total = sum([mid if i > mid else i for i in an])

        if total <= cost:
            if mid > result:
                result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)
