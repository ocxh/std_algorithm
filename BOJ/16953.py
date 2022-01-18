a, b = map(int, input().split())

cnt = 1
while a < b:
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break

    cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)
