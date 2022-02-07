a,b= map(int , input().split(' '))
aCD = []
bCD = []

count = 0
while(True):
  count += 1
  x = int(input())
  if(str(x) == '0 0'):
    break

  if(count <= a):
    aCD.append(int(x))
  else:
    bCD.append(int(x))

result = 0
for i in range(len(aCD)):
  for k in range(len(bCD)):
    if(aCD[i] == bCD[k]):
      result += 1
print(result)



