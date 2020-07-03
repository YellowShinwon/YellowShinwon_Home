arr1 = [6, 10, 2]  #6210
arr2 = [3, 30, 34, 5, 9, 2021, 20, 2]  #9534330

def solution(array):
    answer = ''
    list_compare = []
    for number in array:
        number_str = str(number)
        if   number < 10:
            number_compare = number_str * 4
        elif number < 100:
            number_compare = number_str * 2
        elif number < 1000:
            number_compare = number_str + number_str[0]
        else:
            number_compare = number_str
        number_pair = [number_compare, number_str]
        list_compare.append(number_pair)
    list_compare = sorted(list_compare, key=lambda pair:pair[0], reverse=True)
    for number_compare, number_str in list_compare:
        answer += number_str
    answer = str(int(answer))
    return answer

def solution_try_with_ten(arr):
    answer = ''
    ten = [[],[],[],[],[],[],[],[],[],[]]
    for a in arr:
        b = str(a)[0]
        ten[int(b)].append(str(a))
    for a in ten:
        a.sort(reverse=True)
        print(a)
    return answer



from itertools import permutations
def solution_timeover(arr):
    #permutations take a lot of time when calculate the much number of list
    temp = list(permutations(arr, len(arr)))
    permu = ''
    permu_list = []
    for aa in temp:
        for bb in aa:
            permu += str(bb)
        permu_list.append(permu)
        permu = ''
    ans = max(permu_list)
    return ans



def crazy_solution(numbers):
    def mul(x):
        x = x*3
        return x

    numbers = list(map(str, numbers)) # for 로 하나씩 변화해주는 대신 map 으로 한 번에 변환가능

    numbers_mul = list(map(mul, numbers))
    print(numbers_mul)
    numbers_mul.sort(reverse=True)
    print(numbers_mul)
    numbers.sort(key=lambda x: x*3, reverse=True)
    # print(numbers)
    return str(int(''.join(numbers)))

aa = crazy_solution(arr2)