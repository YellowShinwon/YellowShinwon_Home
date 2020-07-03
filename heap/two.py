stock = 10
dates = [5,10]
supplies = [1,100]
k = 100
# return 2


import heapq
def solution(stock, dates, supplies, k):
    total_need_stock = k
    current_stock = stock

    supplies = [-sup for sup in supplies]
    supply_info_list = list(zip(supplies, dates))
    heapq.heapify(supply_info_list)
    answer = 0

    while total_need_stock > current_stock:
        delivery_stock = get_supply(current_stock, supply_info_list)
        current_stock -= delivery_stock
        answer += 1
    return answer

def get_supply(current_wheat, supply_info_list):
    late_delivery = []
    while True:
        delivery = heapq.heappop(supply_info_list)
        stock, date = delivery
        if date <= current_wheat:
            middle_answer = stock
            break
        else:
            late_delivery.append(delivery)
    for delivery in late_delivery:
        heapq.heappush(supply_info_list, delivery)
    return middle_answer

aa = solution(stock, dates, supplies, k)
print(aa)