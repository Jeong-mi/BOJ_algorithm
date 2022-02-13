import sys
import math

while(True):
  a,b= map(int , sys.stdin.readline().split())
  if a== 0 and b == 0:
    break
  aCD = [int(sys.stdin.readline()) for _ in range(a)]
  bCD = [int(sys.stdin.readline()) for _ in range(b)]

  result = 0 #같은 숫자일 갯수

  for cd in bCD: #배열의 모든 요소 반복
    start = 0
    end = a-1

    while start <= end:
      mid = math.ceil((start + end)/2)

      if(aCD[mid] == cd):
        result += 1
        break
      elif(aCD[mid] > cd):
        end = mid - 1
      elif(aCD[mid] < cd):
        start = mid + 1
print(result)



