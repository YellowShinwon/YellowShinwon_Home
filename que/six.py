prices = [1,2,3,2,3]
#answer = [4,3,1,1,0]

def solution(pri):
    last_val = 0
    temp_list = []
    data_length = len(pri)
    answer = [0] * data_length

    for now_num in range(data_length):
        now_val = pri[now_num]
        if last_val > now_val:
            while 1:
                tnum, tval = temp_list[-1]
                if tval > now_val:
                    answer[tnum] = now_num - tnum
                    temp_list.pop()
                else:
                    break

        temp_list.append([now_num, now_val])
        last_val = now_val
    # print(f'answer: {answer}')

    for num, val in temp_list:
        answer[num] = temp_list[-1][0] - num

    return answer

temp = solution(prices)
print(temp)

def solution_err1(pri): #run_time_error
    last_val = 0
    temp_list = []
    answer = [0] * len(pri)
    for now_num, now_val in enumerate(pri):
        if last_val > now_val:
            while 1:
                tnum, tval = temp_list[-1]
                if tval > now_val:
                    answer[tnum] = now_num - tnum
                    temp_list.pop()
                else:
                    break
        temp_list.append([now_num, now_val])
        last_val = now_val

    for num, val in temp_list:
        answer[num] = temp_list[-1][0] - num

    return answer