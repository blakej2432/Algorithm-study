# 30 배수

import sys

num = list(map(int, sys.stdin.readline().rstrip()))

if sum(num) % 3 == 0:
    num.sort(reverse=True)
    if num[-1] == 0:
        print(''.join(list(map(str, num))))
    else:
        print(-1)
else:
    print(-1)
