from collections import deque

# 문자열을 입력 받아
def isPalindrome(s):
    strs = deque()  # 데크 생성

    for i in s:  # 요소 하나하나 문자인지 검사하여 소문자로 변경해 데크에 저장
        if i.isalnum():
            strs.append(i.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # 맨 앞 요소와 맨 뒤 요소를 비교하며 pop
            return False

    return True


# 결과 확인
print(isPalindrome(input()))
