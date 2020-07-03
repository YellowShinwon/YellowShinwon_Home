citations = [3, 0, 6, 1, 5]
# citations = [5, 5, 5, 0]
# return = 3

def solution(citations):
    sort_citations = sorted(citations)
    sort_citations_length = len(sort_citations)
    target_start = 0
    target_list = []
    for count in range(sort_citations_length):
        cite = sort_citations[count]
        if cite > sort_citations_length:
            target_list = sort_citations[count:]
            break
        target_start = cite
        sort_citations_length -= 1

    target_length = len(target_list)
    if target_start > target_length:
        return target_start
    else:
        return target_length

def sexy_solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

def genius_solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

def solution_keep(citations):
    sort_citations = sorted(citations)
    sort_citations_length = len(sort_citations)
    h_index = 0
    for cite in sort_citations:
        if cite <= sort_citations_length:
            h_index = cite
        else:
            break
        sort_citations_length -= 1

    return h_index

a= genius_solution(citations)
print(a)