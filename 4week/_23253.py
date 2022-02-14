import sys

n, m = map(int, sys.stdin.readline().split(' '))

# m개의 리스트를 가진 2차원 배열 초기화하기
#[ [], [], [] ,,, m개 ]
dummy = [[0] for _ in range(m)]

result = '' #결과값 출력하는 변수

for i in range(m):
  k = int(input()) #더미에 쌓인 교과서의 수
  dummy[i] = [0 for _ in range(k)] #k개 길이의 더미 배열
  dummy[i] = list(map(int, sys.stdin.readline().strip().split(' ')))

print(dummy)

for i in range(m):
  is_sorted = (sorted(dummy[i], reverse=True) == dummy[i]) #내림차순으로 정렬된 배열인지 확인
  if(not is_sorted): #정렬된 배열이 아니라면 반복문 나가기
    result = 'No'
    break
  result = 'Yes'
print(result)

