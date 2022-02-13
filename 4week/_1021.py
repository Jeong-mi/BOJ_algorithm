from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split(' '))

locations = sys.stdin.readline().strip().split(' ') #마지막에 붙는 개행문자 제거 후 ' '로 분리하기

dq = deque([i for i in range(1, n+1)]) #원형 큐로 구현하기


