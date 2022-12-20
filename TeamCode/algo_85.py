

import sys

n = int(sys.stdin.readline().strip())
seq = [0] * (n+3)

seq[0] = 1
seq[1] = 2
seq[2] = 3

for i in range(3, n+1):

	if i%2 == 1:
		seq[i] = seq[i-3]
	elif i%2 == 0:
		seq[i] = seq[i-1] + i

	if i == n:
		print(seq[i])

