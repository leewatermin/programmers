import heapq

def solution(operations):
    heap = []
    heap_max = []
    heap_len = 0
    
    for i in range(len(operations)):
        if operations[i].split(" ")[0] == "I":
            heapq.heappush(heap, int(operations[i].split(" ")[1]))
            heapq.heappush(heap_max, (-1)*int(operations[i].split(" ")[1]))
            heap_len += 1
        
        elif heap_len > 0:
            heap_len -= 1
            if operations[i].split(" ")[1] == "1": 
                heap.remove((-1)*heapq.heappop(heap_max))
            else:
                heapq.heappop(heap)
    
    return [0, 0] if heap_len == 0 else [(-1)*heapq.heappop(heap_max), heapq.heappop(heap)]
