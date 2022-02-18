#시간초과오류
import sys

n = int(sys.stdin.readline())

dots = []
for _ in range(n):
  dot = tuple(map(int, sys.stdin.readline().split(' ')))
  dots.append(dot)

Xs = []
Ys = []
count = 0
for i in range(n):
  for k in range(i+1, n):
    if(dots[i][0] == dots[k][0]): #x좌표 같은지 확인 (y축에 평행)
      if not dots[i][0] in Xs: #같다면 중복되지 않도록
        Xs.append(dots[i][0])
        count += 1
      else:
        continue
    if(dots[i][1] == dots[k][1]): #y좌표 같은지 확인 (x축에 평행) 
      if not dots[i][1] in Ys: #같다면 중복되지 않도록
        Ys.append(dots[i][1])
        count += 1
      else:
        continue
    else:
      continue
print(Xs)
print(Ys)
print(count) 
  