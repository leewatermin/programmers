def solution(number, k):
    origin_len = len(number)
    num_list = [number[0]]

    for num in number[1:]:
        while num_list and num_list[-1]<num and k>0:
            num_list.pop()
            k -= 1 
        num_list.append(num)
        
    if len(number) > origin_len - k: return number[0:origin_len-k]
    
    return "".join(num_list)
