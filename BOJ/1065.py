x = int(input())

if x < 9:
    cnt = x
else:
    cnt = 9
    for i in range(10, x + 1):
        buffer = list(map(int, str(i)))
        dt = buffer[1] - buffer[0]
        flag = True
        for j in range(1, len(buffer)):
            if buffer[j] - buffer[j - 1] != dt:
                flag = False
        if flag:
            cnt += 1

print(cnt)
