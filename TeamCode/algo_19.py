# 가장 큰 수
# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항


def solution(numbers):
    numbers.sort(key=lambda num: str(num)*3, reverse=True)
    paste = ''
    for i in numbers:
        paste += str(i)
    return str(int(paste))

# 문자인 숫자를 비교할 땐 사전방식이다. 그걸 기억하고 num * 3해서 큰 수 만드는 거 기억하자