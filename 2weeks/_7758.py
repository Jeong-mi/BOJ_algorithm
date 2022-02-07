record = {}

n = int(input())
for i in range(n): #4라면 4개의 로그가 있음
  key, value = input().split(' ')
  record[key] = value
print(record)

person = []
for k,v in record.items():
  if(v == 'enter'):
    person.append(k)
person.sort(reverse=True) #내림차순 정렬
print(person)
for i in range(len(person)):
  print(person[i])


    