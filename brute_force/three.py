baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
from itertools import permutations
def solution(baseball):
    number_list = list(permutations(['1','2','3','4','5','6','7','8','9'],3))
    candidate_list = []
    answer = 0
    for baseball_number, strike, ball in baseball:
        if strike == 3:
            answer = 1
            break
        temp = what_is_this_function(baseball_number, number_list, strike, ball)
        candidate_list.append(temp)
    answer_list = candidate_list.pop()
    for candidate in candidate_list:
        answer_list = list(set(answer_list) & set(candidate))
    answer = len(answer_list)
    return answer

def what_is_this_function(baseball_number, number_list, strike, ball):
    possible_list = []
    temp_strike, temp_ball = 0, 0
    baseball_number = list(str(baseball_number))
    for candidate_number in number_list:
        for one_digit in range(0,3):
            for two_digit in range(0,3):
                if baseball_number[one_digit] == candidate_number[two_digit]:
                    if one_digit == two_digit:
                        temp_strike += 1
                    else:
                        temp_ball += 1
        if temp_strike == strike and temp_ball == ball:
            possible_list.append(candidate_number)
        temp_strike, temp_ball = 0, 0
    return possible_list



solution(baseball)
