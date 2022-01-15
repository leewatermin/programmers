def solution(bridge_length, weight, truck_weights):
    now = [0 for i in range(bridge_length)]
    now_weigh = 0
    how_many = len(truck_weights)
    sec = 0
    cnt = 0
    
    while True:
        sec += 1
        if now[0] != 0:
            cnt += 1  
            now_weigh -= now[0]
        del now[0]
        
        if how_many == cnt: return sec
        if (len(truck_weights)>0):
            if now_weigh + truck_weights[0] <= weight:
                now_weigh += truck_weights[0]
                now_truck = truck_weights.pop(0)
                now.append(now_truck)
            else: now.append(0)
