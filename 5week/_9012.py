# ( 개수와 )개수가 같다고 YES가 나오진 않는다..
import sys

n = int(sys.stdin.readline())

sum = 0
result = []

for i in range(n):
  data = list(sys.stdin.readline().strip())

  for t in data:
    if(t == '('):#여는 괄호일 땐 sum +1
      sum += 1
    elif(t == ')'):#닫는 괄호일 땐 sum -1
      sum -= 1
      if(sum < 0): #하나씩 검사하면서 닫는 괄호가 더 많아졌다면
        break      #닫는 괄호가 더 많아졌다면 괄호 한 쌍이 될 기회가 이젠 없기 때문에
    
  if(sum == 0):
    result.append('YES')
  else:
    result.append('NO')
  sum = 0

for i in range(n):
  print(result[i])

