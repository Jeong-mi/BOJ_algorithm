n = int(input())

card = []
for i in range(n):
  card.append(i+1)

while True:
  if(len(card) == 1):
    print(card[0], end=" ")
    break
  print(card[0], end=" ")
  del card[0]
  card.append(card[0])
  
  del card[0]
