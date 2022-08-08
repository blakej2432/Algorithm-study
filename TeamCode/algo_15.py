# 최소직사각형
# 문제 설명
# 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

# 아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

# 명함 번호	가로 길이	세로 길이

def solution(sizes):
    result_a = []
    result_b = []
    for i in sizes:
        result_a.append(max(i[0],i[1]))
        result_b.append(min(i[0],i[1]))
    answer = max(result_a)*max(result_b)
    return answer

# 이 풀이 참조

# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)
