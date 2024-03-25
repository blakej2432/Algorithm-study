# 성격 유형 검사하기

score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

def solution(survey, choices):
    answer = ''
    for s, c in zip(survey, choices):
        if c > 4:
            score[s[1]] += c - 4
        if c < 4:
            score[s[0]] += 4 - c
    
    score_li = list(score.items())
    for i in range(0, len(score)-1, 2):
        if score_li[i][1] >= score_li[i+1][1]:
            answer += score_li[i][0]
        else:
            answer += score_li[i+1][0]
        
    return answer