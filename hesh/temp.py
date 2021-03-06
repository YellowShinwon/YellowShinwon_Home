import itertools

def baseball_fun(x, y):
    x = list(x)
    y = list(y)
    s = 0
    b = 0  # 스트라이크, 볼
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i:
                s += 1
            else:
                b += 1
    return [s, b]

def solution(baseball):
    v = list(map(lambda x: str(x[0]), baseball))  # 질문하는 숫자
    r = list(map(lambda x: [x[1], x[2]], baseball))  # 질문에 대한 답

    all = list(itertools.permutations(range(1, 10), 3))  # 모든 가능한 수
    all = list(map(lambda x: list(map(str, x)), all))  # change to str

    cnt = 0  # 가능한 수
    for x in all:
        if [baseball_fun(x, y) for y in v] == r: cnt += 1

    return cnt
