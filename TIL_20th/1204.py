T = int(input())
for i in range(T):
    N = int(input())
    list1 = list(map(int, input().split()))
    dic1 = {} 
    
    for i in list1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 0
    print("#" + str(N), max(dic1 , key = dic1.get))       