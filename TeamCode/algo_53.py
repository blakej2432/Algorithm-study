# 소믈리에

# 이렇게 풀면 시간초과. 문제 원리를 이해하고 역으로 카운팅할 생각해보자

# 최댓값 빼고 나머지를 채우는 과정이 반복이다? -> 반복하면서 최대값을 하나씩 빼서 최소값과 같아지게하는 반복 수를 카운트. 카운트라서 결국엔 같다
import sys

N = int(sys.stdin.readline().rstrip())

glass = list(map(int, sys.stdin.readline().split()))

cnt = 0
while True:
	glass.sort()
	cnt += 1
	for i in range(N-1):
		glass[i] = glass[i] + 1
	
	if len(set(glass)) == 1:
		print(cnt)
		break

# k = 0
# while True:
# 	check = ((max(glass)*N - sum(glass)) + N*k) 
# 	if (check % (N-1) == 0) and max(glass):
# 		print(check, max(glass)*N, (max(glass)*N - sum(glass)),k)
# 		print(int(check/(N-1)))
# 		break
# 	k += 1

# 8 4 7 8 7 7 7

# 12 12 11 12 9 9 13

# 1 1 2 2 2 2 5
# 2 2 3 3 3 3 5
# 3 3 4 4 4 4 5
# 4 4 5 5 5 5 5
# 5 5 6 6 6 6 5
# 6 6 6 7 7 7 6
# 7 7 7 7 8 8 7
# 8 8 8 8 8 9 8
# 9 9 9 9 9 9 9

	
# 1 5 2 1 2 2 2
# 2 5 3 2 3 3 3 
# 3 5 4 3 4 4 4
# 4 5 5 4 5 5 5
# 5 6 5 5 6 6 6
# 6 7 6 6 7 7 6
# 7 7 7 7 8 8 7
# 8 8 8 8 9 8 8
# 9 9 9 9 9 9 9