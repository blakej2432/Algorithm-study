# 대회 or 인턴 

import sys

N, M, K = map(int, sys.stdin.readline().split())

cnt = 0
while True:
    N -=2
    M -=1
    if N<0 or M<0 or (N+M) < K:
        break
    cnt += 1
print(cnt)






