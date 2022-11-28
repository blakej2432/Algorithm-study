# 상처 반창꼬 붙이기

import sys

N = int(sys.stdin.readline().rstrip())

knee = []
for i in range(N):
	knee.append(list(map(int, sys.stdin.readline().split())))
	
wound = []
for i in range(N):
	for j in range(N):
		if knee[i][j] == 1:
			wound.append((i,j))

max_v = max(wound)[0]
max_h = max(wound, key = lambda x: x[1])[1]
min_v = min(wound)[0]
min_h = min(wound, key = lambda x: x[1])[1]


print((max_v - min_v + 1)*(max_h - min_h + 1))

