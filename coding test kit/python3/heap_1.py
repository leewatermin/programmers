import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    for i in range(len(scoville)):
        if scoville[0] < K and len(scoville) == 1:
            return -1
        elif scoville[0] < K:
            heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        else: return i
    return -1
