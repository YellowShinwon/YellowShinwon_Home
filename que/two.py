bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# 100	100	[10,10,10,10,10,10,10,10,10,10]	110
#return = 8
#bridge_length, weight, truck_weights
#처음 들어간 친구는 bridge_length만큼 움직이면 끝!
def solution(bridge_length, weight, truck_weights):
    sum, count = 0, 0
    bridge=[]
    for temp in range(bridge_length+1):
        bridge.append([])
    while truck_weights:
        # ENTER THE BRIDGE
        if sum + truck_weights[0] <= weight:
            sum += truck_weights[0]
            bridge[-1].append(truck_weights.pop(0))
        # IN THE BRIDGE
        for position in range(1, len(bridge)):
            #initial
            if bridge[position] == []: continue
            truck = bridge[position].pop(0)
            bridge[position-1].append(truck)
            if position == 1: sum -= bridge[0][-1]
        count += 1
    return count + bridge_length

def solution_old():
    sum, count = 0, 0
    bridge=[]
    for temp in range(bridge_length+1):
        bridge.append([])
    bridge.append(truck_weights)
    while bridge[-1]:
        for position in range(1, len(bridge)):
            #initial
            if bridge[position] == []: continue
            elif position == len(bridge) - 1:
                if sum + bridge[-1][0] > weight: continue
                truck = bridge[position].pop(0)
                bridge[position - 1].append(truck)
                sum += truck
            elif position == 1:
                truck = bridge[position].pop(0)
                bridge[position-1].append(truck)
                sum -= truck
            else:
                truck = bridge[position].pop(0)
                bridge[position-1].append(truck)
        count += 1
    return print(count + bridge_length)


solution(bridge_length, weight, truck_weights)