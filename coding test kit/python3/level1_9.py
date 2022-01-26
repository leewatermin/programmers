def solution(d, budget):
    d = sorted(d, reverse = False)
    for i in range(len(d)): 
        budget -= d[i]
        if budget == 0: return i+1
        elif budget < 0: return i
    return len(d)
