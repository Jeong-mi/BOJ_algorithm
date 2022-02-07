from collections import deque

n, k = map(int , input().split(' '))
queue = deque([i for i in range(1, n+1)])
print(queue) ##deque([1, 2, 3, 4, 5, 6])

result = []
for i in range(n): #7명이면 7번 반복하면 된다
  queue.rotate(-(k-1))
  print(queue)
  result.append(queue[0])
  queue.popleft()
  print(queue)
  print("===")

result = ', '.join(str(s) for s in result)

print('<'+result+'>')