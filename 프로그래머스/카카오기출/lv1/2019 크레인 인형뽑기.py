# pseudo code
'''
moves에 따라 열의 맨 위 원소 0으로 바꾸고 stack에 쌓기
stack에 새로 쌓인 원소가 기존에 있던 원소와 같으면 기존 원소와 함께 삭제
삭제 될 경우 cnt += 2
return cnt
'''

# my code
def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if stack and stack[-1] == board[j][i-1]:
                    stack.pop()
                    answer += 2
                
                else:
                    stack.append(board[j][i-1])
                    
                board[j][i-1] = 0
                break
                
    return answer


# others'
'''
if stack 으로 stack 비어있는지 확인하는거 보다 애초에
stack = [0] 으로 설정해서 비었을 때 indexerror 피할 수 있다.
'''