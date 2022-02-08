from collections import defaultdict
import sys

n = int(sys.stdin.readline())

#유사딕셔너리 사용 : dict 클래스의 서브 클래스
xDots = defaultdict(list) #y가 key, x가 value
yDots = defaultdict(list) #x가 key, y가 value

for i in range(n):
  x, y  = map(int, input().split(' '))
  xDots[x].append(y)
  yDots[y].append(x)

count = 0
for i in xDots.keys():
  if(len(xDots[i]) >= 2):
    count+= 1

for i in yDots.keys():
  if(len(yDots[i]) >= 2):
    count+= 1
print(count)
