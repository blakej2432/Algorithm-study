# 지뢰찾기 (알고리즘 위클리 1주차)

# 입력
# 4 4
# *...
# ....
# .*..
# ....

# 출력
# *100
# 2210
# 1*10
# 1110

import sys

M, N = map(int,sys.stdin.readline().split())

array = []
for i in range(N):
	array.append(sys.stdin.readline().rstrip())

lst = []
for i in array:
	elem = []
	for j in i:
		if j == '.':
			elem.append(0)
		else:
			elem.append(j)
	lst.append(elem)

nx = [1,-1,0,0,1,1,-1,-1]
ny = [0,0,1,-1,1,-1,1,-1]

for i in range(N):
	for j in range(M):
		if lst[i][j] == '*':
			continue
		for z in range(8):
			dx = nx[z]
			dy = ny[z]
			if 0<=i+dy<N and 0<=j+dx<M:
				if lst[i+dy][j+dx] == '*':
					lst[i][j] += 1


for i in lst:
	print(''.join(map(str, i)))
			
			
			