a,b= map(int , input().split(' '))
aCD = []
bCD = []

count = 0
while(True):
  count += 1
  x = input()
  if(x == '0 0'):
    break

  if(count <= a):
    aCD.append(int(x))
  else:
    bCD.append(int(x))

result = 0
for i in range(a):
  for k in range(b):
    if(aCD[i] == bCD[k]):
      result += 1
print(result)



