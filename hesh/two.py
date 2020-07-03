def solution(phone_book): #2.34 / 0.03
    dic = {}
    for num in phone_book:
        dic[num] = len(num)

    for num in phone_book:
        value = dic[num]
        for num2 in phone_book:
            if value < dic[num2]:
                str_key2 = num2
                if str_key2[:value] == num:
                    return False

    return True

def solution_two(phone_book): # 4.12ms / 0.04ms
    phone_book.sort(key=lambda x: len(x))
    print(phone_book)
    for a in range(len(phone_book)): #1,2,3,4,5,6
        for b in range(a+1, len(phone_book)):
            if phone_book[a] == phone_book[b][:len(phone_book[a])]:
                return False
    return True


phone_book = ['119', '97674223', '1195524421', '123', '456', '789']
solution_two(phone_book)

