# 달리기 경주

def solution(players, callings):
    answer = []
    pl_dict = {value: idx for idx, value in enumerate(players)}
    
    for call in callings:
        ord_now = pl_dict[call]
        ord_fast = ord_now - 1 
        
        players[ord_now] = players[ord_fast] 
        players[ord_fast] = call
        
        pl_dict[call] -= 1
        pl_dict[players[ord_now]] += 1
        
    answer = players
    
    return answer