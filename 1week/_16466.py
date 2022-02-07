selledNum = int(input())
selledTicket = list(map(int, input().split(' '))) #정수 리스트로 반환

selledTicket.sort() #[1, 2, 4, 7, 8]
pointer = 1 #하나씩 증가시킨다

for i in range(selledNum):
  if(selledTicket[i] != pointer):
    break
  pointer +=1
print(pointer)
      