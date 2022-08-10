# 프린터
# 문제 설명
# 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

def solution(priorities, location):
    order = []
    idx = [i for i in range(len(priorities))]

    while len(priorities) > 0:
        if priorities[0] < max(priorities):
            a = priorities.pop(0)
            priorities.append(a)
            b = idx.pop(0)
            idx.append(b)
        else:
            a = priorities.pop(0)
            b = idx.pop(0)
            order.append(b)
            if b == location:
                return len(order)

# from collections import deque
# def solution(priorities, location):
#     queue = deque([(idx, k) for idx, k in priorities])
#     answer = 0
#     while True:
#         cur = queue.popleft()
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer

# 이렇게 (인덱스, 값) 저장하고 값끼리 인덱스끼리 비교하려면 any(for문) 이용하면 되잖어