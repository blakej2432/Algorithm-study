# RGB 거리

import sys

N = int(sys.stdin.readline().rstrip())

lst = []

for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    lst[i][0] = min(lst[i-1][1], lst[i-1][2]) + lst[i][0]
    lst[i][1] = min(lst[i-1][0], lst[i-1][2]) + lst[i][1]
    lst[i][2] = min(lst[i-1][0], lst[i-1][1]) + lst[i][2]

print(min(lst[N-1]))





