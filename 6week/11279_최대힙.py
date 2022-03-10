import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = [] #heap이라는 빈 리스트를 생성

for _ in range(n):
  x = int(input())
  print("입력: ",x)
  if(x != 0): #원소가 0이 아니라면
    heapq.heappush(heap, (-x, x)) #heapq의 함수를 호출하면서 원소를 각각 추가해준다
    
  else:       #원소가 0이라면
    if len(heap): #만약 빈 배열이 아니라면
      max_item = heapq.heappop(heap)[1] 
      #heappop을 하면 최댓값이 반환된다, 실제 원소값은 튜플의 두번째자리이므로 [1]
      print('출력:', end=" ")
      print(max_item)
      
    else:         #빈 배열이라면
      print('출력:', end=" ")
      print(0)
  print('heap:', heap)


# 최대힙? 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙
#* heap = [1,3,5,7,9]인 리스트라면
#힙 자료형에 (-x, x) 형태의 튜플로 넣어준다면 튜플의 첫번째 원소를 우선순위로 힙을 구성하게 된다
#* [(-9, 9), (-7, 7), (-5, 5), (-3, 3), (-1, 1)]
#원소값의 부호를 바꿨기 때문에, 최소 힙으로 구성된 heapq 모듈을 최대 힙으로 구현할 수 있게 된다.


#참고링크: https://littlefoxdiary.tistory.com/3