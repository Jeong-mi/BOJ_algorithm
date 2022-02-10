import itertools
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]

permu = list(itertools.permutations(cards, k))

result = set() #중복제거
for i in permu: #각 튜플(i)의 값이 정수인데 join 안은 str이어야 한다
  result.add(''.join((map(str, i))))
print(len(result))
