T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b:
        k = c
        print("#" + str(i), c)
    else:
        if a == c:
            k = b
            print("#" + str(i), b)
        else:
            k = a
            print("#" + str(i), a)
