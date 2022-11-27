# 로또

import sys

def dfs(start, depth):
    
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        # end =' '썼을 때 계속 이어서 안나오고 밑에 줄로 떨구는 역할    
        print()
        # 함수 종료
        return

    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
    
combi = [0 for i in range(13)]

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()


