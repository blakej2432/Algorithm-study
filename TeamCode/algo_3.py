# 없는 숫자 더하기
# 문제 설명
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

num = list(range(10))

def solution(numbers):
    answer = 0
    for i in num:
        if i not in numbers:
            answer += i
    return answer

# for i in range(10) 바로 하면 되잖어
