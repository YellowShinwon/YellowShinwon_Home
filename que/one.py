heights=[1,5,3,6,7,6,5]
# [0,0,2,0,0,5,6]
def solution():
    list_len = len(heights)
    answer = [0] * list_len
    for tx_count in range(list_len):
        for rx_count in range(tx_count, -1, -1):
            if heights[rx_count] > heights[tx_count]:
                answer[tx_count] = rx_count+1
                break
    return answer
