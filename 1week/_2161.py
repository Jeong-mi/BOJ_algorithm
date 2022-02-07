n = int(input())

card = []
for i in range(n):
  card.append(i+1)

while True:
  if(len(card) == 1):
    print(card[0], end=" ")
    break
  print(card[0], end=" ") #[1, 2, 3, 4, 5, 6, 7]
  del card[0]          #[2, 3, 4, 5, 6, 7]
  card.append(card[0]) #[2, 3, 4, 5, 6, 7, 2]
  
  del card[0]          #[3, 4, 5, 6, 7]
