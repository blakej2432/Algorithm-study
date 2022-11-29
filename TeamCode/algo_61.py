# 01타일

import sys

N = int(sys.stdin.readline().rstrip())

d = [0]*1000001
d[1] = 1
d[2] = 2

def tile(N):
	for i in range(3, N+1):
		d[i] = (d[i-1] + d[i-2]) % 15746

print(tile(N) % 15746) 