# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

t = int(sys.stdin.readline().rstrip())

lst = []
for i in range(t):
	lst.append(list(map(int, sys.stdin.readline().split())))

for i in lst:
	answer = 0
	l, s, n, k, m, *V = i
	if s/l < n/100:
		answer = 1
		
	for i in V:
		if i < m:
			answer = 0

print(answer)






