#종료 조건 없음
def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()




#종료 조건 존재
def recursive_function2(i):
    if i==100:
        return
    
    recursive_function2(i+1)
    print(i,'번째 재귀함수 종료')

recursive_function2(1)