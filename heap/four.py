# operations	= ['I 16','D 1']
# return = [0,0]
operations = ['I 7','I 6','I -5','D -1']
# return = [7,5]

import heapq
def solution(operations):
    data = []
    direction = -1
    for element in operations:
        command, code = element.split()
        code = int(code)
        if command == 'I':
            heapq.heappush(data, code)
        else:
            try:
                direction, data = delete_max_min(code, direction, data)
            except(IndexError):
                pass
    try:
        answer = return_max_min(direction, data)
    except(IndexError):
        answer = [0,0]
    return answer

def convert_max_min(data):
    data = [-number for number in data]
    heapq.heapify(data)
    return data

def delete_max_min(command, direction, data):
    if data == []:
        return direction
    if command != direction:
        data = convert_max_min(data)
        heapq.heappop(data)
        direction = command
    else:
        heapq.heappop(data)
    return direction, data

def return_max_min(direction, data):
    if direction == 1:
        max = (-1)*heapq.heappop(data)
        data = convert_max_min(data)
        min = heapq.heappop(data)
    else:
        min = heapq.heappop(data)
        data = convert_max_min(data)
        max = (-1)*heapq.heappop(data)
    return max, min


hey = solution(operations)
print(f'answer={hey}')