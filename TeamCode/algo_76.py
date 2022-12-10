# 숫자 카드 2

import sys
from bisect import bisect_left, bisect_right


card=list(map(int, sys.stdin.readline().split()))
card=sorted(card)

target_list=list(map(int, sys.stdin.readline().split()))

answer_sheet=[]
for target in target_list:
  answer=bisect_right(card, target)-bisect_left(card, target)
  answer_sheet.append(answer)

for output in answer_sheet:
  print(output, end=' ')














