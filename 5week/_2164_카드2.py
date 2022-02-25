import sys
from collections import deque

n = int(input())
queue = deque([i+1 for i in range(n)])
print(queue)
while(len(queue) > 1):
  queue.popleft()
  queue.rotate(-1) #왼쪽으로 이동
print(queue[0])
