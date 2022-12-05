# 정수 삼각형

import sys

N = int(sys.stdin.readline().rstrip())

lst = []

for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(len(lst[i])):
        if j == 0:
            lst[i][j] = lst[i-1][j] + lst[i][j]
        elif j == i:
            lst[i][j] = lst[i-1][j-1] + lst[i][j]
        else:
            lst[i][j] = max(lst[i-1][j-1], lst[i-1][j]) + lst[i][j]

print(max(lst[N-1]))
