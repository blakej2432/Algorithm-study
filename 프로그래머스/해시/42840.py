# 모의고사

def solution(answers):
    answer = []
    
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len_1 = len(pattern_1) 
    len_2 = len(pattern_2)
    len_3 = len(pattern_3)
    
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    for i in range(len(answers)):
        num_1 = i % len_1
        num_2 = i % len_2
        num_3 = i % len_3
        
        if answers[i] == pattern_1[num_1]:
            score_1 += 1
        if answers[i] == pattern_2[num_2]:
            score_2 += 1
        if answers[i] == pattern_3[num_3]:
            score_3 += 1
    
    scores = [score_1, score_2, score_3]
    
    max_score = max(scores)
    
    for idx, score in enumerate(scores):
        if score == max_score:
            answer.append(idx + 1)
            
    return answer