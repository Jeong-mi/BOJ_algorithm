import sys
import heapq
input = sys.stdin.readline

n=int(input())
abs_heap=[]

for _ in range(n):
  x = int(input())
  print("입력, ",x)

  if(x != 0): #원소가 0이 아니라면
    #heapq의 함수를 호출하면서 원소를 각각 추가해준다
    heapq.heappush(abs_heap, (abs(x), x))
  else:
    if len(abs_heap): #만약 빈 배열이 아니라면
      #배열에서 절대값이 가장 작은 원소값 찾기
      min_item = abs_heap[0][0]
      #절대값이 가장 작은 원소가 여러개일 수 있으므로 배열로 저장
      #min_items = [i for i, v in enumerate(abs_heap) if min _item == v[0]]
    

      print(abs_heap)
      
    else:         #빈 배열이라면
      print('출력:', end=" ")
      print(0)
print(abs_heap)
