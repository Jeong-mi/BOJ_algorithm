import sys

T = int(sys.stdin.readline()) #테스트 케이스 개수

for t in range(T):
  n = int(sys.stdin.readline()) #상품의 수
  case = list(map(int, sys.stdin.readline().strip().split(' '))) #2n개의 정수 입력
  
  price = [] #정가를 넣어두는 리스트
  discount = [] #할인가를 넣어두는 리스트

  while(len(case) != 0): #case 원소가 없어질 때까지
    normal = int(case[0] / 0.75) #할인가에 대응하는 정가 가격

    for i in range(len(case)):
      if(normal == case[i]): 
        price.append(case.pop(i)) #case에서 정가에 해당하는 원소 추출해서 price에 넣기
        discount.append(case.pop(0)) #case에서 할인가에 해당하는 원소 추출해서 discount에 넣기
        break

  print("Case #%d: " %(t+1), end="")
  for i in range(len(discount)):
    print(discount[i], end=" ")
  print()
  

# 첫 인덱스부터 시작해서 두개원소를 제거하면서 리스트에 아무것도 없어질 때까지
# 첫번째 원소는 가장 작은 원소이므로 무조건 할인된 원소일 것이다.
# 첫번째 원소에 대응하는 정가인 원소를 찾으면서 쭉쭉..
# 입력된 리스트를 하나 만들고
# 정가를 넣어두는 리스트, 할인가를 넣어두는 리스트도 만듬
# 입력된 리스트에서 하나씩 처리하면서 pop하면서 쭉쭉..