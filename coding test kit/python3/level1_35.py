a, b = map(int, input().strip().split(' '))
for i in range(0, b):
    tmp = ''
    for j in range(0, a): tmp += '*'
    print(tmp)
    
