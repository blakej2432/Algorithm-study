# 파도반 수열

import sys


def P(N):
	d = [0] * 101
	d[1] = 1
	d[2] = 1
	d[3] = 1
	for i in range(4, 101):
		d[i] = d[i-2] + d[i-3]
	return d[N]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
	N = int(sys.stdin.readline().rstrip())
	print(P(N))


