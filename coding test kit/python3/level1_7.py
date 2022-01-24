def solution(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if sosu(nums[i]+nums[j]+nums[k]) == True: cnt += 1
    return cnt
                
def sosu(num):
    for i in range(2, num-1):
        if num%i == 0: return False
    return True
