# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬)

arr = [1, 2, 3, 4, 5]
total = 0

""" for i in arr:
    if i > 2:
        total += i """

total = sum([i for i in arr if i > 2])

print(total)
