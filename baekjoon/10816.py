from bisect import bisect_left, bisect_right

n = int(input())
an = list(map(int, input().split()))
m = int(input())
am = list(map(int, input().split()))
an.sort()


def bisect(arr, target):
    right = bisect_right(arr, target)
    left = bisect_left(arr, target)
    counting = right - left
    return counting


for i in am:
    print(bisect(an, i), end=" ")
