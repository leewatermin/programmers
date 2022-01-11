def solution(lottos, win_nums):
    rank = {'6': 1, '5': 2, '4': 3, '3': 4, '2': 5}
    zero = 0
    cnt = 0
    answer = [0 for i in range(2)]
    
    for num in lottos:
        if num == 0: zero +=1
        for win in win_nums:
            if num == win:
                cnt += 1
                
    if cnt+zero >= 2: answer[0] = rank[str(cnt+zero)]
    else: answer[0] = 6
    if cnt >= 2: answer[1] = rank[str(cnt)]
    else: answer[1] = 6
        
    return answer
