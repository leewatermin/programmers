import heapq
import math

def solution(jobs):
    answer = 0
    sec = 0
    task_left = len(jobs)
    jobs = sorted(jobs)
    
    while task_left > 0:
        task = []
        for i in range(len(jobs)):
            if jobs[i][0] <= sec and jobs[i][1] > 0:
                heapq.heappush(task, (jobs[i][1], i))
        if len(task) > 0:
            task_tmp = heapq.heappop(task)
            answer += sec - jobs[task_tmp[1]][0] + task_tmp[0]
            sec += jobs[task_tmp[1]][1]
            jobs[task_tmp[1]] = (0, 0)  
            task_left -= 1
        else: sec += 1
            
    return math.floor(answer/len(jobs))
