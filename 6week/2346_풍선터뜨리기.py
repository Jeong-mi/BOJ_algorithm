from collections import deque

n = int(input())
ballon = deque(list(map(int, input().split(' '))))

print(ballon) #ballon=[3,2,1,-1,-1]

for i in range(n):
  c = ballon.popleft()
  print(ballon)
  print("==")
  ballon.rotate(-(c+1))
  print(ballon)
