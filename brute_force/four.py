brown, yellow = 10, 2 # return=[4,3]
# brown, yellow = 8, 1 # return=[3,3]
# brown, yellow = 24, 24 # return=[8,6]
# 8 <= brown <= 5,000

def solution(brown, yellow):
    core_list = core_combination(yellow)
    shell = shell_calculator(core_list, brown)
    return shell

def core_combination(yellow):
    root_yellow = int(yellow**(1/2)) + 1
    core_list = []
    for num in range(1, root_yellow):
        if yellow % num == 0:
            core_list.append([yellow//num, num])
    return core_list

def shell_calculator(core_list, brown):
    for width, length in core_list:
        shell_width = width +2
        shell_length = length +2
        shell = (shell_width*shell_length)-(width*length)
        if shell == brown:
            break
    return [shell_width, shell_length]



solution(brown, yellow)