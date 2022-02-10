from collections import defaultdict
import sys

works = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
inp = input()
print(inp)
if inp in works.keys():
  works[inp] += 1
print(works)
