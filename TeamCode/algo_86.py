# 기약분수

import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
for i in range(1, int((n+1)/2)):
	for j in range(i, 0, -1):
		if i%j == 0 and (n-i)%j == 0:
			GCD = j
			break

	if GCD == 1:
		cnt += 1

print(cnt)

