genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays= [500, 600, 150, 800, 2500]

#[4, 1, 3, 0]
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
        print(dic_result)
        song_rank = sorted(dic_result.items(), key=lambda items: items[1], reverse=True)

        count = 0
        for song in song_rank:
            if count == 2:
                break
            answer.append(song[0])
            count\
                += 1
    return answer


def solution_two():
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


import operator
from collections import defaultdict

class Music:
    def __init__(self, id, g, p):
        self.id = id
        self.g = g
        self.p = p

def solution(genres, plays):
    db = []
    g_db = defaultdict(int)
    for i in range(len(genres)):
        db.append(Music(i,genres[i],plays[i]))
        g_db[genres[i]] += plays[i]
    db.sort(key=operator.attrgetter("id"))
    db.sort(key=operator.attrgetter("p"),reverse=True)

    g_db = sorted(g_db.items(),key=operator.itemgetter(1), reverse=True)

    result = []
    for g in g_db:
        idx = 0
        cnt = 0
        while cnt <2:
            if idx >= len(db):
                break
            if db[idx].g == g[0]:
                result.append(db[idx].id)
                cnt += 1
            idx += 1
    return result