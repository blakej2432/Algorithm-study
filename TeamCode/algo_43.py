# 나는야 포켓몬 마스터 이다솜(실버4)
# 포켓몬 도감에 번호랑 이름 저장되어있고 새로 마주치는 거 마다 번호는 이름을 이름은 번호를 출력


import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

N_dict = defaultdict(str)
for i in range(1, N+1):
    N_dict[i] = sys.stdin.readline().rstrip()

dict_reversed = {value:key for key, value in N_dict.items()}

for i in range(M):
    a = sys.stdin.readline().rstrip()
    # 번호 출력, 이름 출력 테크닉
    try:
        print(N_dict[int(a)])
    except:  
        print(dict_reversed[a])