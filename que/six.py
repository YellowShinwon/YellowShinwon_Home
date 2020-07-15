prices = [1,2,3,2,3]
#answer = [4,3,1,1,0]

from collections import deque
def solution(prices):
    length = len(prices)
    answer = [0] * length
    now_time = 0

    prices = deque(prices)
    last_price = prices.popleft()
    stack = [[last_price, now_time]]

    for now_price in prices:
        now_time += 1
        while stack and stack[-1][0] > now_price:
            pprice, ttime = stack.pop()
            answer[ttime] = now_time - ttime
        stack.append([now_price, now_time])

    while stack:
        pprice, ttime = stack.pop()
        answer[ttime-1] = now_time - ttime

    return answer

temp = solution(prices)
print(temp)
