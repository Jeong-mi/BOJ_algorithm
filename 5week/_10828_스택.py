import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
  command = sys.stdin.readline().split()
  if(command[0] == 'push'):
    stack.append(command[1])
  elif(command[0] == 'pop'):
    if(len(stack) == 0):
      print(-1)  
    else:
      print(stack[-1])
      stack.pop()
  elif(command[0] == 'size'):
    print(len(stack))
  elif(command[0] == 'empty'):
    if(len(stack) == 0):
      print(1)
    else:
      print(0)
  elif(command[0] == 'top'):
    if(len(stack) == 0):
      print(-1)
    else:
      print(stack[-1])

# input()은 sys.stdin.readline()와 비교해서 
# prompt 메시지를 출력하고
# 개행문자를 삭제한 값을 리턴하기 때문에 느리다
# sys.stdin.readline().split() -> 여러개를 한줄에 입력받아 리스트로 저장된다