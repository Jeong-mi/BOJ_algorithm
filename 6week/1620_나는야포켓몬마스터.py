import sys
input = sys.stdin.readline

n, m = map(int, input().split())

book_number = {} #포켓몬 - 인덱스 구조
book_pokemon = {} #인덱스 - 포켓몬 구조

for i in range(1, n+1):
  pokemon = input().strip() #개행문자 제거해주기
  book_number[pokemon] = i
  book_pokemon[i] = pokemon
#book_number = {'Bulbasaur': 1, 'Ivysaur': 2, ...}
#book_pokemon = {1: 'Bulbasaur', 2: 'Ivysaur', ...}


for _ in range(m):
  s = input().strip() # 개행문자 제거해주기

  if(s.isdigit()):    # 숫자형인지 판별해주는 함수        
    print(book_pokemon[int(s)]) # 숫자로 바꿔주고 해당 인덱스의 포켓몬 출력

  elif(s.isalpha()): # 문자열인지 판별해주는 함수
    print(book_number[s])  # 해당 포켓몬의 인덱스 출력

