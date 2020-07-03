priorities = [1,2,3,9,5,6,7,9,7,8,8] #14
# priorities = [1,1,9,1,1,1]
location = 0
# return = 5

from collections import deque
def best_solution(pri, loc):
    dq = deque([(i, p) for i, p in enumerate(pri)])
    answer = 0
    while True:
        cur = dq.popleft()
        if any(cur[1] < q[1] for q in dq):
            dq.append(cur)
        else:
            answer += 1
            if cur [0] == loc:
                return answer


def solution(pri, loc):
    count, back = 0, 0
    target = pri[loc]
    pri[loc] = 0
    for lv in range(9, target, -1):
        lv_loc = []
        sw, tc, loc_m = 0, 0, 0
        for ii in range(len(pri)):
            if lv == pri[ii]:
                sw = 1
                count += 1
                tc += 1
                lv_loc.append(ii)
        if sw == 1:
            dc = 0
            for ii in lv_loc:
                del pri[ii-dc]
                dc += 1
            temp_list = pri
            pri = temp_list[lv_loc[-1]-tc+1:]
            pri = pri + temp_list[:lv_loc[-1]-tc+1]

    for ii in pri:
        if ii == 0: return count + 1
        elif ii == target: count += 1

    return 0

temp = solution(priorities, location)
print(temp)


def solution_first(pri, loc): # ~2,11,17,18,19
    count = 0
    target = pri[loc]
    len_pri = len(pri)
    last_loc = 0

    for lv in range(9, target, -1):
        for ii in range(len_pri):
            if pri[ii] == lv:
                count += 1
                last_loc = ii
    if last_loc < loc:
        temp_list = pri[last_loc:loc]
        for ii in temp_list:
            if ii == target:
                count += 1
    elif last_loc > loc:
        temp_list = pri[last_loc+1:]
        for ii in temp_list:
            if ii == target:
                count += 1
        temp_list = pri[:loc]
        for ii in temp_list:
            if ii == target:
                count += 1
    else: return count+1
    return count + 1
