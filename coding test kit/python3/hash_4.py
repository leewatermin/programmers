def solution(genres, plays):
    original = []
    songs_per_genre = []
    dict_genre = {}
    answer  = []
    
    for i in range(len(genres)):
        original.append((genres[i], plays[i]))
        if genres[i] in dict_genre: dict_genre[genres[i]] += plays[i]
        else: dict_genre[genres[i]] = plays[i]
    dict_genre = sorted(dict_genre.items(), key = lambda item: item[1], reverse = True)
    
    for key in dict_genre:
        for j in range(len(original)):
            if original[j][0] == key[0]: songs_per_genre.append((original[j][1], j))
        songs_per_genre = sorted(songs_per_genre, key=lambda song: song[0], reverse = True)
        answer.append(songs_per_genre[0][1])
        if len(songs_per_genre) > 1: answer.append(songs_per_genre[1][1])
        songs_per_genre = []
        
    return answer
