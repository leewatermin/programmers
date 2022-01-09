def solution(prices):
    answer = [0 for i in range(len(prices))]
    for cursor in range(len(prices)):
        for nxt in range(cursor+1,len(prices)):
            if prices[cursor] <= prices[nxt]: answer[cursor] += 1
            elif prices[cursor] > prices[nxt]: 
                answer[cursor] += 1
                break
    return answer
