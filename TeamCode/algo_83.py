
# 실패율
def solution(N, stages):
    d = [0] * (N+2)
    
    for i in stages:
        d[i] += 1
    
    failure = []
    num_player = len(stages)
    for i in range(1, N+1):
        if num_player == sum(d[:i]):
            failure.append([i,0])
        else:
            failure.append([i,d[i] / (num_player - sum(d[:i]))])
    
    answer = []
    for i in sorted(failure, key = lambda x : x[1], reverse=True):
        answer.append(i[0])
    
    return answer






