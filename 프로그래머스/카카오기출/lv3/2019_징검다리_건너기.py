# pseudo code
'''
모두 탐색하는 것은 시간 제한에 걸림
건널 수 있는 최대 명수 (정답)을 가정하여 이분탐색으로 찾아낸다.
stones의 최소값, 최대값을 양 끝점으로 잡고 mid를 최대 명수로 가정
건너는 돌 개수가 k보다 작을 경우 최소값을 mid + 1, 반대의 경우 최대값을 mid - 1
최소값과 최대값이 일치하는 곳에서 mid가 찾고자하는 정답
'''



# my code
def solution(stones, k):
    left = min(stones)
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        jump = 0
        for stone in stones:
            if stone <= mid:
                jump += 1
            else:
                jump = 0
            if jump >= k:
                break
        if jump < k:
            left = mid + 1
        else:
            right = mid - 1
    return left
        