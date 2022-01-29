from collections import deque

n = int(input())

queue = deque([i for i in range(1, n+1)])
print(queue) #deque([1, 2, 3, 4, 5, 6])
#print(len(queue)) #6
#dequeue는 pop이 불가능하다! popleft()를 사용해야 한다!

idx = 0
stg = 1

for i in range(n-1): #사람수-1 만큼 단계를 진행
  print("\nstg", stg)

  idx = ((stg**3) - 1) % len(queue)
    
  print("idx", idx)
  print(queue)

  queue.rotate(-idx)
  print(queue)

  queue.popleft()
  print(queue)

  idx = 0
  stg += 1

print(queue[0])
