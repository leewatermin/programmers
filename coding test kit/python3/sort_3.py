def solution(citations):
    for i in range(max(citations), 0, -1):
        cnt = 0
        for c in citations:
            if c >= i: cnt += 1
        if cnt >= i: return i
    return 0
