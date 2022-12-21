# 폭탄 터뜨리기


import sys
from collections import deque


n, m, k =  map(int, sys.stdin.readline().split())

jido = []
for i in range(n):
	jido.append(list(map(int, sys.stdin.readline().split())))


def bfs(i, j):
	global m
	
	queue = deque([i,j])
	
	while queue:
		i, j = queue.popleft()
		k = jido[i-1][j-1]
		
		for a in range(1, k+1):
			if i-1 + a >= 0 and i-1 + a < n:
				if jido[i-1 + a][j-1] != 0:
					queue.append([i-1 + a, j-1])
					jido[i-1 + a][j-1] = 0
					m -= 1
			if j-1 + a >= 0 and j-1 + a < n:
				if jido[i-1][j-1 + a] != 0:
					queue.append([i-1, j-1 + a])
					jido[i-1][j-1 + a] = 0
					m -= 1
					
			if i-1 - a >= 0 and i-1 - a < n:
				if jido[i-1 - a][j-1] != 0:
					queue.append([i-1 - a, j-1])
					jido[i-1 - a][j-1] = 0
					m -= 1
			if j-1 - a >= 0 and j-1 - a < n:
				if jido[i-1][j-1 - a] != 0:
					queue.append([i-1, j-1 - a])
					jido[i-1][j-1 - a] = 0
					m -= 1
					
while True:
	q, w = map(int, sys.stdin.readline().split())
	bfs(q, w)
	m -= 1









