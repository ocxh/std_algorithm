m, n = map(int, input().split())
s = list(map(int, input().split()))
s.sort(reverse=True)

start = 1
end = max(s)

result = 0


def binary_search(start, end, result):
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for i in s:
            if i < mid:
                break
            count += i // mid

        if count >= m:
            if result < mid:
                result = mid
            start = mid + 1
        else:
            end = mid - 1
    if count == 0:
        return 0
    return result


print(binary_search(start, end, result))
