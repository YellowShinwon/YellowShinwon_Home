
arrangement = '()(((()())(())()))(())'

def solution(arr):
    answer, sticks = 0, 0
    laser_to_zero = arr.replace('()', '0')
    for bracket in laser_to_zero:
        if bracket == '(':
            sticks += 1
        elif bracket == '0':
            answer += sticks
        else:
            answer += 1
            sticks -= 1
    return answer

def my_solution(arr):
    open_bracket = []
    open_bracket = []
    answer = 0
    for bracket in arr:
        if bracket == '(':
            open_bracket.append(0)
            answer += 1
        else:
            open_bracket.pop()
            if last_bracket != bracket:
                answer += len(open_bracket) - 1
        last_bracket = bracket
    return answer


def solution_timeover(arr):
    #layer
    open_bracket = []
    bar = []
    for num, bracket in enumerate(arr):
        if bracket == '(':
            open_bracket.append(1)
        else:
            count = open_bracket.pop()
            if count == 1:
                for num in range(len(open_bracket)):
                    open_bracket[num] += 1
            else:
                bar.append(count)
    answer = sum(bar)
    return answer

temp = solution(arrangement)
print(temp)


from collections import deque
def solution_0428(arr):
    #making layers
    layer = deque([])
    arr_list = deque([(num, let)for num, let in enumerate(arr)])
    while arr_list:
        pair = []
        for num in range(len(arr_list)-1):
            if arr_list[num][1] == '(' and arr_list[num+1][1] == ')':
                pair.append([num, arr_list[num][0], arr_list[num+1][0]])
        l_len = len(pair)
        for ii in range(l_len-1, -1, -1):
            del arr_list[pair[ii][0]+1]
            del arr_list[pair[ii][0]]
        layer.append(pair)

    laser = layer.popleft()
    answer = 0
    #calculation
    while layer:
        one_layer = layer.pop()
        for one_bar in one_layer:
            bar_sep = 1
            for x in laser:
                if one_bar[1] < x[1] and x[1] < one_bar[2]:
                    bar_sep += 1
            answer += bar_sep
    return answer
