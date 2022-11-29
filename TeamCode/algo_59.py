# 알고리즘 수업 - 피보나치 1

import sys

n = int(sys.stdin.readline().rstrip())

cnt_1 = 0
def fibo_1(n):
	global cnt_1
	if n == 1 or n == 2:
		cnt_1 += 1
		return 1
	else:
		return fibo_1(n-2) + fibo_1(n-1)

cnt_2 = 0
d = [0] * 41
d[1] = 1
d[2] = 1

def fibo_2(n):
	global cnt_2
	for i in range(3,n+1):
		cnt_2 += 1
		d[i] = d[i-2] + d[i-1]
	return d[n]

fibo_1(n)
fibo_2(n)

print(cnt_1, cnt_2)