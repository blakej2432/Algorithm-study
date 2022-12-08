# 큐 2

import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

# 리스트 비어있는지 확인하기 -> if not queue, 무조건 len()으로 하려하지말자
queue = deque()
def Q(x):
	if x[0] == 'empty':
		if not queue:
			print(1)
		else:
			print(0)
	if x[0] == 'size':
		print(len(queue))
	if x[0] == 'push':
		queue.append(x[1])
	if x[0] == 'pop':
		if not queue:
			print(-1)
		else:
			print(queue.popleft())
	if x[0] == 'front':
		if not queue:
			print(-1)
		else:
			print(queue[0])
	if x[0] == 'back':
		if not queue:
			print(-1)
		else:
			print(queue[-1])



for _ in range(N):
	Q(sys.stdin.readline().split())












