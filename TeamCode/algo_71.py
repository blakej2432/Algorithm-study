# 4방향 로봇


import sys

n, m, k = map(int, sys.stdin.readline().split())
move = sys.stdin.readline().rstrip()

lst = []

for i in range(n):
	lst.append([0]*m)

lst[0][0] = 1

a = 0
b = 0
for i in range(k):
	if move[i] == 'E':
		if 0 <= a < n and 0 <= b-1 < m:
			lst[a][b-1] += 1
			a = a
			b = b-1
		else:
			lst[a][b] += 1

	if move[i] == 'W':
		if 0 <= a < n and 0 <= b + 1 < m:
			lst[a][b+1] += 1
			a = a
			b = b+1
		else:
			lst[a][b] += 1

	if move[i] == 'N':
		if 0 <= a-1 < n and 0 <= b < m:
			lst[a-1][b] += 1
			a = a-1
			b = b
		else:
			lst[a][b] += 1

	if move[i] == 'S':
		if 0 <= a+1 < n and 0 <= b < m:
			lst[a+1][b] += 1
			a = a+1
			b = b 
		else:
			lst[a][b] += 1

# 2차원에서 최대값 뽑기
print(max(map(max,lst)))
