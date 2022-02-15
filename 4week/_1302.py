# 디렉터리에
# 입력받은 값을 key와 비교해서 있으면 value값 +=1
# 없으면 새로운 k-v생성 후 value=1로 설정하기

n = int(input())

books = {}
for _ in range(n):
  name = input()
  if(name in books.keys()):
    books[name] += 1
  else:
    books[name] = 1

max = max(books.values()) # 팔린 책의 max 값
bestSeller = []  #가장 많이 팔린 책을 저장하는 리스트

for k, v in books.items():
  if(max == v):
    bestSeller.append(k)

bestSeller.sort() #사전순 정렬
print(bestSeller[0])
