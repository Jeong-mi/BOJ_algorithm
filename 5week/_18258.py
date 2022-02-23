import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
  command = sys.stdin.readline().split()

  if(command[0] == 'push'):
    queue.append(command[1])
  elif(command[0] == 'pop'):
    if len(queue):
      print(queue[0])
      queue.popleft()
    else:
      print(-1)
  elif(command[0] == 'size'):
    print(len(queue))
  elif(command[0] == 'empty'):
    if(len(queue)):
      print(0)
    else:
      print(1)
  elif(command[0] == 'front'):
    if len(queue):
      print(queue[0])
    else:
      print(-1)
  elif(command[0] == 'back'):
    if len(queue):
      print(queue[-1])
    else:
      print(-1)

# list로 선언해서 pop(0)을 하게 되면,
# 첫번째 요소를 pop 하고 나서 나머지 요소들의 인덱스를 1칸씩 당기는 과정에서 O(n) 계산량 발생
# 따라서 deque를 사용