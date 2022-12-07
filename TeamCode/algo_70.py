# 괄호

import sys

N = int(sys.stdin.readline().rstrip())


for i in range(N):
    bracket = list(sys.stdin.readline().rstrip())
    stack = []
    for j in bracket:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                print('NO')
                stack.append(j)
                break
            else:
                stack.pop()
          
    if len(stack) == 0:
        print('YES')
    elif stack[-1] == '(':
        print('NO')


