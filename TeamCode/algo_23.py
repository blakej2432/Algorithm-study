# 완주하지 못한 선수
# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.


def solution(participant, completion):
    if set(participant) - set(completion):
        return list(set(participant) - set(completion))[0]

    else:
        participant.sort()
        completion.sort()
        for i, k in zip(participant, completion):
            if i != k:
                return i

def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('0')
    for i, k in zip(participant, completion):
        if i == k:
            continue
        return i

# collections 이용한 풀이
# import collections

# a = ['a','b','c','d']
# b = ['a','c','d']

# list((collections.Counter(a) - collections.Counter(b)).keys())[0]

