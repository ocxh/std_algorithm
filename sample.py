# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬

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
