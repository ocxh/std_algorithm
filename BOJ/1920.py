n = int(input())
an = list(map(int, input().split()))
m = int(input())
am = list(map(int, input().split()))
an.sort()


def binary_search(an, target):
    start = 0
    end = len(an) - 1
    mid = (start + end) // 2
    offset = 0
    while start <= end:
        if an[mid] == target:
            offset = 1
            break
        elif an[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    if offset == 1:
        return 1
    else:
        return 0


for i in am:
    print(binary_search(an, i))
