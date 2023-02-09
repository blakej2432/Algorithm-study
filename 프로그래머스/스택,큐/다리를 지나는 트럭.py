# pseudo code
'''
다리를 건너는 중인 트럭 수 세팅하는 리스트 생성
건널 수 있는 조건이 되면 트럭을, 안되면 0을 append
결국 건너는 중인 트럭이 없다면 종료
'''


# my code
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer