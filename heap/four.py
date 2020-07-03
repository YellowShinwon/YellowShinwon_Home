operations	= ['I 16','D 1']
# return = [0,0]
operations = ['I 7','I 5','I -5','D -1']
# return = [7,5]

def solution(operations):
    for command in operations:
        command, code = command.split()

solution(operations)