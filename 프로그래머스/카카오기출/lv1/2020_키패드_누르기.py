# pseudo code
'''
키 간의 거리를 구해야하므로 딕셔너리로 키의 좌표를 설정해놓는다.
left, right가 확정된 키를 처리한다.
둘 다 가능한 키는 좌표간 거리를 계산해서 더 가까운 쪽의 손을 선택하도록 한다.
'''

# my code
def solution(numbers, hand):
    answer = ''
    num_dict = {1 : (0, 0), 2 : (0,1), 3 : (0,2),
               4: (1, 0), 5: (1, 1), 6: (1, 2),
               7: (2, 0), 8: (2, 1), 9: (2, 2),
               '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    L = '*'
    R = '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            L = num
        elif num in [3, 6, 9]:
            answer += 'R'
            R = num
        else:
            now_row, now_col = num_dict[num][0], num_dict[num][1]
            L_row, L_col = num_dict[L][0], num_dict[L][1]
            R_row, R_col = num_dict[R][0], num_dict[R][1]
            
            if abs(now_row - L_row) + abs(now_col - L_col) == \
            abs(now_row - R_row) + abs(now_col - R_col):
                if hand == 'left':
                    answer += 'L'
                    L = num
                else:
                    answer += 'R'
                    R = num
            elif abs(now_row - L_row) + abs(now_col - L_col) < \
            abs(now_row - R_row) + abs(now_col - R_col):
                answer += 'L'
                L = num
            else:
                answer += 'R'
                R = num
            
    return answer

# others'
def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    left_s = dic['*']
    right_s = dic['#']
    
    for i in numbers:
        now = dic[i]
        # 1, 4, 7을 누르는 경우 무조건 왼손
        if i in [1, 4, 7]:
            answer += 'L'
            left_s = now
            
        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif i in [3, 6, 9]:
            answer += 'R'
            right_s = now
            
        # 2, 5, 8, 0을 누르는 경우
        else:
            left_d = 0
            right_d = 0
            
            # 좌표 거리 계산해주기
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                left_s = now
                
            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                right_s = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    left_s = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    right_s = now
            
    return answer