# 신나는 함수 실행

import sys

# 이 두개가 어떻게 다를 수가 있지? - 위 오답, 아래 답
d = [[[0] * 3] * 3] * 3
dp = [[[0 for _ in range(3)] for _ in range (3)] for _ in range (3)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if d[a][b][c] : # 이미 값이 존재하면 재귀를 안들어가고 저장해놓은거에서 뽑아버려
        return d[a][b][c]

    if a<b<c :
        d[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        d[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    return d[a][b][c]


while True:
	a, b, c = map(int, sys.stdin.readline().split())
	if a == -1 and b == -1 and c == -1:
		break
	print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
