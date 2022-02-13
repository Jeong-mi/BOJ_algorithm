from collections import defaultdict
import sys

n = int(sys.stdin.readline())

#유사딕셔너리(dict 클래스의 서브 클래스) 사용 : 하나의 key값에 여러 값들을 넣어줄 수 있는 자료형
#딕셔너리의 value의 default를 리스트로 생성해서 활용
xDots = defaultdict(list) #x가 key, y가 value인 xDots 딕셔너리 생성
yDots = defaultdict(list) #y가 key, x가 value인 yDots 딕셔너리 생성

for i in range(n):
  x, y  = map(int, input().split(' '))
  xDots[x].append(y) #리스트 함수를 사용할 수 있게 됨
  yDots[y].append(x)

count = 0
for i in xDots.keys(): # y축 평행 => x값 같은 게 있다
  if(len(xDots[i]) >= 2): #하나의 key 값에 2개 이상의 value값이 있다면 증가시킴
    count+= 1

for i in yDots.keys():  # x축 평행 => y값 같은 게 있다
  if(len(yDots[i]) >= 2):
    count+= 1
print(xDots, yDots)
print(count)
