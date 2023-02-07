# pseudo code 
'''
n명을 기준으로 할 경우 시간초과, 시간의 최소값을 기준으로 이분탐색
1분, max(times) * n 을 최소값, 최대값으로 설정
mid // time -> 시간동안 심사관이 심사할 수 있는 총 사람 수
초과, 미만에 따라 left right 조절
'''


# my code
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer

hand = 'right'

a = ''

a += hand

a = [0, 0]
b = [1, 1]
abs(a-b)