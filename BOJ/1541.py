s = input()
result = 0
# -가 없는 식이면 전부 합한게 정답
if len(s.split("-")) == 1:
    s = s.split("+")
    s = map(int, s)
    print(sum(s))
# -가 1개라도 있으면
else:
    s = s.split("-")
    # 첫번째 -부분이 위치한곳 뒤는 모두 더한 후 음수값으로 만듬
    for i in range(1, len(s)):
        buffer = s[i].split("+")
        for j in range(len(buffer)):
            result += int(buffer[j])
    result *= -1
    first = s[0].split("+")
    # 첫번째 - 가 위치한 앞 부분은 추가로 더하기(모두 양수)
    for i in range(len(first)):
        result += int(first[i])
    print(result)
