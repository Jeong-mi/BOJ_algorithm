import sys
input = sys.stdin.readline

n,m = map(int, input().split())

sets = set()

for _ in range(n):
  sets.add(input().strip())

cnt = 0

for _ in range(m):
  test = input().strip()
  if test in sets:
    cnt += 1

print(cnt)

#trie 알고리즘으로도 풀어보기
#Trie 알고리즘이란? 입력되는 문자열을 트리 형식으로 만들어 진행되어 빠르게 문자열을 찾도록 하는 자료구조
# 보통 O(n)의 시간이 걸린다면 O(m) (m은 문자열 길이) 라는 짧은 시간이 소요됨