def solution(people, limit):
    cnt = 0
    left = 0
    right = len(people)-1
    
    people = sorted(people)

    while left < right:
        if people[left] + people[right] <= limit: left += 1
        right -= 1
        cnt += 1
    if left == right: cnt += 1

    return cnt
