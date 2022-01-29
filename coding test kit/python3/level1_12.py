def solution(x):
    xlist = list(map(int, str(x)))
    xsum = 0
    for i in range(len(xlist)): xsum += xlist[i]
    if x%xsum == 0: return True
    else: return False
