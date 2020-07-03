jobs = [[0, 10], [4, 10], [5, 11], [15, 2]]

import heapq
def solution(jobs):
    total_job_list = jobs
    heapq.heapify(total_job_list)
    first_job = heapq.heappop(total_job_list)

    current_time = first_job[0] + first_job[1]
    total_process_time = current_time - first_job[0]
    count = 1
    available_job_list = []
    while True:
        count += 1
        make_priority_job_list(current_time, available_job_list, total_job_list)
        relative_process_time, current_time = time_calculator(current_time, available_job_list, total_job_list)
        total_process_time += relative_process_time

        if available_job_list == [] and total_job_list == []:
            break
    answer = (total_process_time//count)
    return answer

def make_priority_job_list(current_time, available_job_list, total_job_list):
    while total_job_list!=[]:
        one_job = heapq.heappop(total_job_list)
        if one_job[0] <= current_time:
            available_job = [one_job[1], one_job[0]]
            heapq.heappush(available_job_list, available_job)
        else:
            heapq.heappush(total_job_list, one_job)
            break
    return 0

def time_calculator(current_time, available_job_list, total_job_list):
    if available_job_list == []:
        available_job = heapq.heappop(total_job_list)
        relative_process_time = available_job[1]
        current_time = available_job[0] + available_job[1]
    else:
        available_job = heapq.heappop(available_job_list)
        absolute_process_time, start_time = available_job
        current_time += absolute_process_time
        relative_process_time = current_time - start_time
    return relative_process_time, current_time

a= solution(jobs)
print(f"answer:{a}")