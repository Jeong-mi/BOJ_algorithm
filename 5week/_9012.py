#아직 못 품!!
# ( 개수와 )개수가 같다고 YES가 나오진 않는다..
import sys

n = int(sys.stdin.readline())

case = {'(': 0, ')': 0}
result = []

for i in range(n):
  data = list(sys.stdin.readline().strip())

  for t in data:
    if(t == '('):
      case['('] += 1
    else:
      case[')'] += 1

  if(case['('] == case[')']):
    result.append('YES')
  else:
    result.append('NO')

  case[')'] = 0
  case['('] = 0

for i in range(n):
  print(result[i])

