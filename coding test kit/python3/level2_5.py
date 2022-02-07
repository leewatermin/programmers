def solution(n):
    return F(n) % 1234567

def F(n):
    a, b = 0, 1
    if n <= 1: return n
    else: 
        for i in range(1, n): a, b = b, a + b
    return b
