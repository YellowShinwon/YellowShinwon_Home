# answers = [1,2,3,4,5]
#[1]
answers = [2,1,2,3,2,4,2,5]
#[1,2,3]

#first  = [1,2,3,4,5 반복]
#second = [2,1,2,3,2,4,2,5 반복]
#third  = [3,3,1,1,2,2,4,4,5,5 반복]

def solution(answers):
    people = [[0,1], [0,2], [0,3]]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for number in range(len(answers)):
        first_number = number % 5
        second_number = number % 8
        third_number = number % 10
        if answers[number] == first_number + 1:
            people[0][0] += 1
        if answers[number] == second[second_number]:
            people[1][0] += 1
        if answers[number] == third[third_number]:
            people[2][0] += 1
    result = grade_calculate(people)
    return result

def grade_calculate(people):
    people.sort(reverse=True)
    max = people[0][0]
    result = []
    for person in people:
        print(person)
        if person[0] == max:
            result.append(person[1])
        else: break
    result.sort()
    return result




def solution_let1(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)
    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

aa = solution(answers)
# print(aa)
