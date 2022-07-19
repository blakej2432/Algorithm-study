# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건


# 이게 내가 처음 푼 풀이고, 시간복잡도 적음
a = [1,2,3,4,5] * 2000
b = [2,1,2,3,2,4,2,5] * 1250
c = [3,3,1,1,2,2,4,4,5,5] * 1000

def solution(answers):
    count_lst = []
    for k in [a, b, c]:
        count = 0
        for i in range(len(answers)):
            if answers[i] == k[i]:
                count += 1
        count_lst.append(count)
    return [idx+1 for idx, score in enumerate(count_lst) if score == max(count_lst)]

# 근데 이것도 한번 봐바
a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    count_lst = []
    for k in [a, b, c]:
        count = 0
        for idx, answer in enumerate(answers):
            if answer == k[idx%len(k)]:
                count += 1
        count_lst.append(count)

    return [idx+1 for idx, score in enumerate(count_lst) if score == max(count_lst)]

# idx랑 값이 모두 필요한 뭔가를 하면 enumerate로 뽑을 생각 먼저 해봐
# k[idx % len(k)]  - 인덱스를 순환주기대로 뺑뱽 돌게 만들기. 인덱스를 순환주기로 나눠주면 돼.
