# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬

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
