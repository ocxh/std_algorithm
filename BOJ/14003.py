import sys

input = sys.stdin.readline


def bs(li, num):
    start = 0
    end = len(li)
    while start < end:
        mid = (start + end) // 2
        if li[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


n = int(input())
a = list(map(int, input().split()))
arr = [1] * n
barr = [-1000000001]
res = []


for i in range(n):
    if barr[-1] < a[i]:
        barr.append(a[i])
        arr[i] = len(barr) - 1
    else:
        index = bs(barr, a[i])
        barr[index] = a[i]
        arr[i] = index


max_len = max(arr)
print(max_len)

# n-1부터 0까지 최장거리 요소에 해당하는 값 구하기
for i in range(n - 1, -1, -1):
    if max_len == arr[i]:
        res.append(a[i])
        max_len -= 1


res.reverse()
for i in res:
    print(i, end=" ")
