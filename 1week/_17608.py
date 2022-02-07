import sys

n = int(sys.stdin.readline())

stick = []
for i in range(n):
  stick.append(int(sys.stdin.readline()))

#print(stick) #[6, 9, 7, 6, 4, 6]

cnt = 1 #먼저 마지막 막대기는 무조건 보이므로! 
max = stick[-1] #먼저 마지막 막대기가 가장 클 것이므로!
for i in range(n-1, -1, -1): #n-1부터 -1까지 반복문!
  if(stick[i] > max):
    cnt += 1
    max = stick[i]
print(cnt)