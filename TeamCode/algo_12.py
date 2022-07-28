# 조이스틱
# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자

def solution(name):
    answer = 0
    
    num_list = [min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name]
   
    answer += sum(num_list)
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        
        next_i = i+1
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    
    return answer+min_move

# 왼,오 위,아래를 다 고려 해야 해서 하나씩 넘어가면서 할 수가 없어. 어떨 때 세는지를 세분화해서 추가해주는 식으로 해야해