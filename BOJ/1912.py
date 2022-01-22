n = int(input())
arr = list(map(int, input().split()))

if max(arr) < 0:
    print(max(arr))
else:
    hap = 0
    max_hap = 0
    for i in arr:
        hap += i
        if hap < 0:
            hap = 0
        if hap > max_hap:
            max_hap = hap

    print(max_hap)
