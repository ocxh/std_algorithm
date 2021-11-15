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
