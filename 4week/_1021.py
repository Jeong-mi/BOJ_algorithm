from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split(' '))

#마지막에 붙는 개행문자 제거 후 ' '로 분리하기
#그 후 문자열 배열을 정수형 배열로 변환하기
locations = list(map(int, sys.stdin.readline().strip().split(' '))) 
print(locations)
dq = deque([i for i in range(1, n+1)]) #원형 큐로 구현하기
lo = 0 #뽑으려는 위치값이 들어있는 k의 이터레이터
cnt = 0 #총 이동 횟수

while(lo < k):# k 개수만큼 반복문

  for i in range(0, len(dq)):
    if(dq[i] == locations[lo]):
      case1 = len(dq) - i #오른쪽으로 이동시키는 경우 이동시켜야 하는 횟수
      case2 = i - 0 #왼쪽으로 이동시키는 경우 이동시켜야 하는 횟수
      if(case1 < case2): #case1만큼 오른쪽으로 이동시키기
        dq.rotate(case1)
        cnt += case1
      elif(case1 >= case2): #case2만큼 왼쪽으로 이동시키기
        dq.rotate(-case2)
        cnt += case2
      dq.popleft()
      break

  lo += 1
      
print(cnt)
