scoville = 	[1, 2, 3, 9, 10, 12]
scoville = 	[0,0,0,0,0]
K = 7
# return 2

import heapq
def solution(scoville, K):
    answer = 0
    first_min = 0
    heapq.heapify(scoville)
    while 1:
        try:
            first_min = heapq.heappop(scoville)
            if first_min >= K:
                return answer
            elif first_min == 0:
                return -1
        except(IndexError):
            pass
        try:
            second_min = heapq.heappop(scoville)
        except(IndexError):
            return -1
        heapq.heappush(scoville, first_min + second_min*2)
        answer += 1

aa = solution(scoville, K)
print(aa)
