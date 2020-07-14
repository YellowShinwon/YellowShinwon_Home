numbers = '17' #3
numbers = '011' #2
# fail = 2,6,9,10
# fail = 1,6,9,10

from itertools import permutations
def solution(numbers):
    number_cards = list(numbers)
    number_permutations = make_permutations(number_cards)
    number_candidate, two = delete_even(number_permutations)
    answer = len(number_candidate) + two
    for number in number_candidate:
        number_root = number ** 0.5
        number_root = int(number_root)
        compare_number = 3
        while compare_number <= number_root:
            if number % compare_number == 0:
                answer -= 1
                break
            compare_number += 2
    print(number_candidate, answer)
    return answer

def make_permutations(number_cards):
    number_permutations = []
    number = ''
    for count in range(len(number_cards)):
        for cards in list(permutations(number_cards, count +1)):
            for card in cards:
               number += card
            number_permutations.append(number)
            number = ''
    return number_permutations

def delete_even(number_permutations):
    odd_list = []
    two = 0
    for number in number_permutations:
        number = int(number)
        if number == 1:
            continue
        if number == 2:
            two = 1
            continue
        if number % 2 == 1:
            odd_list.append(number)
    return set(odd_list), two



from itertools import permutations
def solution_eras_(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))

    for i in range(2, int(max(a) ** 0.5) + 1):
        print(max(a) + 1, set(range(i * 2, max(a) + 1, i)))
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)

a = solution_eras_(numbers)
print(a)
