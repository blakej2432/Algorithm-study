# 3진법 뒤집기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.
def solution(n):
    rest = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rest += str(mod)
    return int(rest, 3)

# 몫을 나누어지는 수로 계속 업뎃, int(rest, 3)-> 3진법수를 10진법수로 변환