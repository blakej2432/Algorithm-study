# 두 정수 사이의 합
# 문제 설명
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 제한 조건

def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a,b+1):
            answer += i
    else:
        a, b = b, a
        for i in range(a,b+1):
            answer += i
            
    return answer

def solution(a, b):
    answer = 0
    if a <= b:
        return b*(b+1)/2 - a*(a-1)/2
    else:
        return a*(a+1)/2 - b*(b-1)/2

# for 문 돌려보는 것도 좋지만 수학적인 부분 고려해보자