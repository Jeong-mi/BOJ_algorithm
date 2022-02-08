from collections import defaultdict
import sys

n = int(sys.stdin.readline())

#유사딕셔너리 사용 : dict 클래스의 서브 클래스
#딕셔너리의 value의 디폴트를 리스트로 생성함
xDots = defaultdict(list) #y가 key, x가 value
yDots = defaultdict(list) #x가 key, y가 value

for i in range(n):
  x, y  = map(int, input().split(' '))
  xDots[x].append(y) #리스트 함수를 사용할 수 있게 됨
  yDots[y].append(x)

count = 0
for i in xDots.keys():
  if(len(xDots[i]) >= 2): #하나의 key 값에 2개 이상의 value값이 있다면 증가시킴
    count+= 1

for i in yDots.keys():
  if(len(yDots[i]) >= 2):
    count+= 1
print(xDots, yDots)
print(count)
