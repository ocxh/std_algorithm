n = int(input())
an = list(map(int, input().split()))
m = int(input())
am = list(map(int, input().split()))

an.sort()
start = 0
end = len(an) - 1


def binary_search(start, end, an, target):
    offset = 0
    while start <= end:
        mid = (start + end) // 2
        if an[mid] == target:
            offset = 1
            break
        elif an[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    if offset == 1:
        return 1
    else:
        return 0


for i in am:
    print(binary_search(start, end, an, i), end=" ")
