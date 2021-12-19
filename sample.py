# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬

q = list(input())  # 입력 받은 문자들을 리스트로
q.sort()  # 정렬

# 팰린드롭 만들기
def mk_pd(q):
    arr = ["X" for _ in range(len(q))]
    buffer = ""
    cnt1 = 0
    cnt2 = -1
    while q:
        if len(q) > 1 and q[0] == q[1]:
            arr[cnt1] = q[0]
            arr[cnt2] = q[1]
            cnt1 += 1
            cnt2 -= 1
            del q[0]
            del q[0]
        else:
            buffer = q[0]
            del q[0]
    for i in range(len(arr)):
        if arr[i] == "X":
            arr[i] = buffer
            break

    return arr


# 만들어진게 팰린드롭인지 체크
def ck_pd(arr):
    res = ""
    f = -1
    for i in range(len(arr)):
        if arr[i] != arr[f]:
            return False
        f -= 1
        res += arr[i]
    return True


result = mk_pd(q)
ch = ck_pd(result)

if ch:
    a = "".join(s for s in result)  # 문자열로 변환
    print(a)
else:
    print("I'm Sorry Hansoo")
