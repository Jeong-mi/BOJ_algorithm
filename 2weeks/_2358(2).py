import sys
input = sys.stdin.readline

n = int(input())

xdots = set()
ydots = set()
for i in range(n):
  x, y = map(int, input().split(' '))
  xdots.add(x)
  ydots.add(y) 
print(xdots)
print(ydots)

count = 0
for i in range(n):
  for k in range(i+1, n):
    if(xdots[i] == xdots[k] or ydots[i] == ydots[k]):
      count += 1
print(count)
  