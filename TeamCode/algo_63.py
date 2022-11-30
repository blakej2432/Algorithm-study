# 가장 긴 증가하는 부분수열

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().split()))
dp = [1]*n

for i in range(n) :
    for j in range(i) :
        if array[i] > array[j] :
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

