import sys

n,m = map(int, sys.stdin.readline().split(' '))

a = set() #집합으로 중복되는 값 제거
for _ in range(n):
  a.add(input())

b = set() #집합으로 중복되는 값 제거
for _ in range(m):
  b.add(input())

#중복되는 문자열을 &연산자로 뽑기
# sorted()로 사전순으로 출력
result = sorted(list(a&b))
print(len(result))
for i in result:
  print(i)