# 연속합

import sys

N = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().split()))

d = [0]*N
d[0] = lst[0]
for i in range(1, N):
    d[i] = max(d[i-1]+lst[i], lst[i])

print(max(d))


