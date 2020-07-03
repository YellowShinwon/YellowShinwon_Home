

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]

def solution():
    dic = {}
    for a in clothes:
        if not a[1] in dic:
            dic[a[1]] = 0
        dic[a[1]] += 1

    llist = list(dic.values())
    result = 1
    for a in llist :
         result *= (a+1)

    return result-1

solution()

