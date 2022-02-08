import sys
input = sys.stdin.readline

n = int(input())

dots = [[0]*2 for _ in range(n)] #for문에서 인덱스가 필요하지 않을 때 _를 사용한다
for i in range(n):
  x, y = map(int, input().split(' '))
  dots[i][0] = x
  dots[i][1] = y


result = 0
for i in range(n):
  compare = i+1
  while(compare <= n-1):
    if(dots[i][0] == dots[compare][0]): #x좌표 같은지 확인 (y축에 평행)
      result += 1
    elif(dots[i][1] == dots[compare][1]): #y좌표 같은지 확인 (x축에 평행)
      result += 1
    compare += 1
print(result)
