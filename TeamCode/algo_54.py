# 스나이퍼

import sys

N, M = map(int, sys.stdin.readline().split())

lst = []
for i in range(M):
	lst.append(sys.stdin.readline().rstrip().rstrip('0'))

cnt = 0
for i in lst:
	for j in i[::-1]:
		if j == '0':
			break
		cnt += 1

print(cnt)

