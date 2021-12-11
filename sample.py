# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
lo = [0 for _ in range(n)]
# 해당 arr에서 head랑 가장 가까운 값의 index를 return
def binary_search(arr, head):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > abs(head):
            end = end - 1
        elif arr[mid] < abs(head):
            start = start + 1
        else:
            if mid + 1 < len(arr):
                m1 = arr[mid + 1]
            else:
                m1 = 1000000001
            if head + m1 < head + arr[mid - 1]:
                return mid + 1
            else:
                return mid - 1

    return mid


result = [1000000001, 0, 0]
for i in range(n):
    if lo[i] == 1:
        continue

    temp = binary_search(arr, arr[i])
    now = arr[temp] + arr[i]
    lo[i] = 1
    lo[temp] = 1
    if abs(now) < result[0]:
        result[0] = abs(now)
        result[1] = arr[i]
        result[2] = arr[temp]


del result[0]
result.sort()
print(result[0], result[1])
