# operations	= ['I 16','D 1']
# return = [0,0]
operations = ['I 7','I 5','I -5','D -1']
# return = [7,5]

import heapq
def solution(operations):
    queue = []
    direction = -1    # 지금 min_heap 상태
    for one_oper in operations:
        command, number = one_oper.split()
        number = int(number)
        if command == 'I':
            heapq.heappush(queue, number)
        elif queue != []:
            queue, direction = delete_max_min(number, direction, queue)

    if queue == []:
        return [0,0]
    else:
        answer = return_max_min(direction, queue)
    return answer

def delete_max_min(number, direction, queue):
    if number == direction:
        heapq.heappop(queue)
    else:
        queue = list(map(convert, queue))
        heapq.heapify(queue)
        heapq.heappop(queue)
        direction = number
    return queue, direction

def return_max_min(direction, queue):
    if direction == -1:
        min = heapq.heappop(queue)
        queue = list(map(convert, queue))
        heapq.heapify(queue)
        max = (-1)*heapq.heappop(queue)
    else:
        max = (-1)*heapq.heappop(queue)
        queue = list(map(convert, queue))
        heapq.heapify(queue)
        min = heapq.heappop(queue)
    return [max, min]

def convert(data):
    return (-1*data)

hey = solution(operations)
print(f'answer={hey}')