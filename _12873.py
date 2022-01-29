n = int(input())

tshirt = []
for i in range(n):
  tshirt.append(i+1)
#print(tshirt) [1, 2, 3]

grade = 1 #1단계부터 시작하기

stg = 1
idx = 0
while len(tshirt) > 1:
  idx = idx + (stg**3)-1
  #if idx >= len(tshirt):
  idx = idx % len(tshirt)
  #print(idx, end=",")
  tshirt.pop(idx)
  stg += 1
print()
print(tshirt[0])
  

