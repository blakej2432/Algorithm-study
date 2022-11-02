# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys
t = int(sys.stdin.readline().rstrip())

lst = list(map(int,sys.stdin.readline().split()))

cnt_1 = 0
cnt_2 = 0
for i in lst:
	if i % 2 != 0:
		cnt_1 += 1
	else:
		cnt_2 += 1
		
if cnt_1 == cnt_2:
	print('tie')
else:
	print(max(cnt_1, cnt_2))







