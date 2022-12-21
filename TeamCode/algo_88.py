# 피보나치 파일복사

import sys

T = int(sys.stdin.readline().rstrip())

def f(n):
	if n == 1 or n == 2:
		return 1
	else:
		return f(n-1) + f(n-2)

for _ in range(T):
	n = int(sys.stdin.readline().rstrip())
	k = 2
	sum_f = 1
	while True:
		sum_f += f(k)
		if sum_f >= n:
			print(k-1)
			break
		k += 1

