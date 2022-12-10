# 수 찾기

import sys

N = int(sys.stdin.readline().rstrip())

array_n = list(map(int, sys.stdin.readline().split()))
array_n.sort()
M = int(sys.stdin.readline().rstrip())

array_m = list(map(int, sys.stdin.readline().split()))

for i in array_m:
    start = 0
    end = N-1
    check = False
    while start <= end:
        mid = (start + end)//2
        if array_n[mid] == i:
            check = True
            break
        elif array_n[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if check == True:
        print(1)
    else:
        print(0)