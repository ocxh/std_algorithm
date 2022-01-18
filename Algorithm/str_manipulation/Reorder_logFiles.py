# 로그의 가장 앞 부분은 식별자
# 문자로 구성된 로그가 숫자 로그보다 앞에옴
# 식별자는 순서에 영향x, 문자가 동일한 경우 식별자 순
# 숫자 로그는 입력 순


def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))

    return letters + digits


l = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", " let3 art zero"]
print(reorderLogFiles(l))
