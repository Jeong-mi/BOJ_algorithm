num = int(input())


case =[]
for i in range(num):
  words = input().split(' ') #['this', 'is', 'test]
  reversed_case = ' '.join(words[::-1]) #리스트를 역순정렬후 join함수로 문자열로 변환시킴
  print('Case #%d: %s' % (i+1, reversed_case))

