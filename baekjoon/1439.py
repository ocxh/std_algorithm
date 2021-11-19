s = list(input())
a0 = 0  # 0집합
a1 = 0  # 1집합
count = 1  # now다음 값의 인덱스
now = s[0]  # 시작위치
while count < len(s):
    if now != s[count]:
        if now == "0":
            a0 += 1
        else:
            a1 += 1
    now = s[count]
    count += 1
s.append("2")
# a0과 a1 모두 0이 아닐 때
# 마지막 숫자가 바로 뒤 숫자하고 다르면
if a0 != 0 and a1 != 0 and (now != s[count]):
    if now == "0":
        a0 += 1
    else:
        a1 += 1
if a0 != 0 and a1 != 0:
    print(min(a0, a1))
else:
    print(max(a0, a1))
