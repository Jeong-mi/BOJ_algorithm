from collections import deque
num = int(input())

case = []

for _ in range(num):
  n= int(input())
  case.append(n)

test = deque()
i = 1
k=0

while(test != case): #test와 case가 같아지면 반복문 종료
  
  while(case[k] != i): #
    test.popleft(i)
    i+=1
  test.pop()
  k+=1
  if(k > num):
    break


