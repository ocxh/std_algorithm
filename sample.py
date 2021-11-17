# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬)

n = int(input())
result = 0
while n >= 0:
    if n % 5 == 0:
        result += n // 5
        break
    n -= 3
    result += 1
if n < 0:
    result = -1
print(result)
