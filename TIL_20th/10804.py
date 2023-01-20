T = int(input())

for i in range(1, T+1):
    N = input()
    result = ''
    for j in N[::-1]:
        if j == 'b':
            result += 'd'
        if j == 'd':
            result += 'b'
        if j == 'p':
            result += 'q'
        if j == 'q':
            result += 'p'
    
    print("#" + str(i), result)