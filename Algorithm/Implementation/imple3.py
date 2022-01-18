#실전문제2 왕실나이트

input_pos = input()

column = int(ord(input_pos[0])-int(ord('a'))) + 1
row = int(input_pos[1])

steps = [(-2,1), (-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
result = 0

for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]

    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)