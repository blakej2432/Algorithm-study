# 회의실 배정

import sys

N = int(sys.stdin.readline().rstrip())

meeting_lst = []
for i in range(N):
    meeting_lst.append(tuple(map(int, sys.stdin.readline().split())))

meeting_lst = sorted(meeting_lst, key = lambda x : (x[1], x[0]))


check = meeting_lst[0]
cnt = 1
for i in meeting_lst:
    if check[1] <= i[0]:
        cnt += 1
    check = i

print(cnt)



