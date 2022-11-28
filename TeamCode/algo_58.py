# 집 구하기

import sys

N, M = map(int, sys.stdin.readline().split())

house = [0] * (N+1)

v = map(int, sys.stdin.readline().split())

for i in v:
	house[i] += 1

min_house = min(house[1:])

hap = 0
for i in range(1, N+1):
	if house[i] == min_house:
		hap += i
	
print(hap)

