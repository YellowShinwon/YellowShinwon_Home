import collections
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']
def my_main(participant, completion): #107.45ms/0.63ms
    answer = ''
    count = 0
    participant.sort(key=lambda x: x)
    completion.sort(key=lambda x: x)
    for com_person in completion:
        if com_person != participant[count]:
            answer = participant[count]
            break
        count += 1
    if not answer:
        answer = participant[-1]
    return answer

def solution_first(participant, completion): #76.59ms/0.42ms
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution_second(participant, completion): #61.99ms/0.47ms
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer
