# 제로

import sys

N = int(sys.stdin.readline().rstrip())

stack = []
for i in range(N):
    k = int(sys.stdin.readline().rstrip())
    if k == 0:
        stack.pop()
    else:
        stack.append(k)

print(sum(stack))










