genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]


# [4, 1, 3, 0]
def solution(genres, plays):
    answer = []
    dic_gen = {}
    dic_son = {}

    for a in range(len(genres)):
        if not genres[a] in dic_gen.keys():
            dic_gen[genres[a]] = 0
            dic_son[genres[a]] = []
        dic_gen[genres[a]] += plays[a]
        dic_son[genres[a]].append(a)
    genres_rank = sorted(dic_gen.items(), key=lambda items: items[1], reverse=True)

    for rank in genres_rank:
        dic_result = {}
        for a in dic_son[rank[0]]:
            dic_result[a] = plays[a]
        song_rank = sorted(dic_result.items(), key=lambda items: items[1], reverse=True)

        count = 0
        for song in song_rank:
            if count == 2:
                break
            answer.append(song[0])
            count += 1
    return answer
