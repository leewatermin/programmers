def solution(answers):
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo_score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == supo_1[i%5]:
            supo_score[0] += 1
        if answers[i] == supo_2[i%8]:
            supo_score[1] += 1
        if answers[i] == supo_3[i%10]:
            supo_score[2] += 1
            
    return [i+1 for i, ele in enumerate(supo_score) if ele == max(supo_score)]

