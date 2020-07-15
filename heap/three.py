jobs = [[0, 10], [4, 10], [5, 11], [15, 2]]

import heapq
def solution(jobs):

    heapq.heapify(jobs)
    #set first job
    first_job = heapq.heappop(jobs)
    current_time = first_job[0] + first_job[1]
    process_time = current_time - first_job[0]
    count = 1
    job_candidate = []

    while job_candidate != [] or jobs != []:
        count += 1
        job_candidate, jobs = select_job_list(current_time, job_candidate, jobs)
        relative_process_time, current_time = time_calculator(current_time, job_candidate, jobs)
        process_time += relative_process_time

    answer = (process_time//count)
    return answer

def select_job_list(current_time, job_candidate, jobs):
    print(current_time, job_candidate, jobs)
    while jobs!=[]:
        one_job = heapq.heappop(jobs)
        if one_job[0] <= current_time:
            available_job = [one_job[1], one_job[0]]
            heapq.heappush(job_candidate, available_job)
        else:
            heapq.heappush(jobs, one_job)
            break
    return job_candidate, jobs

def time_calculator(current_time, job_candidate, jobs):
    if job_candidate == []:
        available_job = heapq.heappop(jobs)
        relative_process_time = available_job[1]
        current_time = available_job[0] + available_job[1]
    else:
        available_job = heapq.heappop(job_candidate)
        absolute_process_time, start_time = available_job
        current_time += absolute_process_time
        relative_process_time = current_time - start_time
    return relative_process_time, current_time

a= solution(jobs)
print(f"answer:{a}")