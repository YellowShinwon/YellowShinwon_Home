
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#return = [5, 6, 3]

def solution(arr, com):
    answer = []
    for a_com in com:
        a_arr = arr[a_com[0]-1:a_com[1]]
        a_arr.sort()
        answer.append(a_arr[a_com[2]-1])
    return answer

aa = solution(array, commands)
print(aa)