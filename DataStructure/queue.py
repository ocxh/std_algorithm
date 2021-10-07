from collections import deque

#큐 구현을 위한 deque 라이브러리
queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(1)
queue.append(0)
queue.popleft()

print(queue)
queue.reverse()
print(queue)