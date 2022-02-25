num = int(input())

stack = []
result = []
cnt = 1

#스택: LIFO

for _ in range(num):
  n = int(input()) # 현재 pop돼야할 수 

  while(cnt <= n): # n이 스택의 마지막에 들어갈 때까지 스택에 추가해주기
    stack.append(cnt)
    cnt+=1
    result.append('+')

  if(stack[-1] == n): # 스택에서 pop할 값이 입력한 n과 같다면 => 수열가능
    stack.pop()
    result.append('-') #다르다면 => 수열 불가능, 종료
  else: 
    print('NO')
    exit(0)

for i in result:
  print(i)


